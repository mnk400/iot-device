'''
Created on Feb 14, 2020

@author: manik
'''
import logging
import threading
import smbus
import numpy as np
from labs.common import SensorData
from sense_hat import SenseHat
from labs.module04 import SensorDataManager
from time import sleep

logging.getLogger("tempReaderLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class HI2CSensorAdapterTask(object):
    '''
    Class which reads the temperature data from the SenseHAT.
    Stores the data in the SensorData class and then further
    calls SensorDataManager to parse the stored data.
    '''

    HUMID_ADDR = 0x5F
    CTRL_REG1  = 0x20
    CTRL_REG2  = 0x21
    
    def __init__(self):
        '''
        Constructor
        '''
        #Calling thread constructor
        threading.Thread.__init__(self)

        #Creating a SensorData instance and setting it's name
        self.sensor_data = SensorData.SensorData()
        self.sensor_data.setName("I2CBus Sensor Data")

        #SMBus instance
        self.i2cReader = smbus.SMBus(1)
        pass

    def run(self):
        '''
        Method to read new data from the senseHat.
        Data is then pushed to the SensorData instance,
        then a sensorDataManager instance is called which overtakes execution.
        '''
        data = self.parseI2CData()

        #Add data to sensorData
        self.sensor_data.addValue(data)

        #Generate a detailed string
        tempString = self.generateString()

        #Log the data and send the sensorData instance in the SensorDataManager
        logging.info(tempString)
        return True   

    def parseI2CData(self) -> float:
        #Defining number of bits
        bits = 8

        #self.initI2CBus()
        #Read calibration relative humidity LSB (ADC) data
        h0_out_l = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x36))
        h0_out_h = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x37))
        h1_out_l = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x3A))
        h1_out_h = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x3B))

        #Read relative humidity (% rH) data
        h0_rh_x2 = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x30))
        h1_rh_x2 = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x31))

        #make 16 bit values (bit shift)
        H0_T0_OUT = np.int16(h0_out_h << 8 | h0_out_l)
        H1_T0_OUT = np.int16(h1_out_h << 8 | h1_out_l)

        #Humidity calibration values
        H0_rH = float(h0_rh_x2 / 2.0)
        H1_rH = float(h1_rh_x2 / 2.0)

        #Solve the linear equations 'y = mx + c' to give the
        #calibration straight line graphs for temperature and humidity
        h_gradient_m = (H1_rH - H0_rH) / (H1_T0_OUT - H0_T0_OUT)
        h_intercept_c = H1_rH - (h_gradient_m * H1_T0_OUT)

        #Read the ambient humidity measurement
        h_t_out_l = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x28))
        h_t_out_h = np.uint8(self.i2cReader.read_byte_data(self.HUMID_ADDR, 0x29))

        #Make 16-bit value 
        H_T_OUT = np.int16(h_t_out_h << 8 | h_t_out_l)

        #Calculate ambient humidity
        H_rH = (h_gradient_m * H_T_OUT) + h_intercept_c

        #Returning the calculated value.
        return H_rH

    def initI2CBus(self) -> bool:
        #Power down the device (clean start)
        self.i2cReader.write_byte_data(self.HUMID_ADDR, self.CTRL_REG1, 0x00)

        #Turn on the humidity sensor analog front end in single shot mode
        self.i2cReader.write_byte_data(self.HUMID_ADDR, self.CTRL_REG1, 0x84)

        #Run one-shot measurement (temperature and humidity). The set bit will be reset by the
        #sensor itself after execution (self-clearing bit)
        self.i2cReader.write_byte_data(self.HUMID_ADDR, self.CTRL_REG2, 0x01)
        return True

    def generateString(self) -> str:
        '''
        Generate a detailed string from a sensorData instance and returns it.
        '''
        msgString  = "\nHumidity from i2c"
        msgString += "\n\tTime : " + self.sensor_data.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensor_data.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensor_data.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensor_data.getCount())
        return msgString

        