'''
Created on Feb 6, 2020

@author: manik
'''
import logging
from labs.common import SensorData
from sense_hat import SenseHat
from labs.module03 import SensorDataManager

logging.getLogger("tempReaderLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class TempSensorAdapterTask(object):
    '''
    Class which reads the temperature data from the SenseHAT.
    Stores the data in the SensorData class and then further
    calls SensorDataManager to parse the stored data.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        #Creating a SensorData instance and setting it's name
        self.sensor_data = SensorData.SensorData()
        self.sensor_data.setName("Temperature Sensor Data")
        #SenseHat instance to interact with the senseHAT
        self.sense = SenseHat()
        #clearing matrix
        self.sense.clear()
        #SensorDataManager instance
        self.sensorDataManager = SensorDataManager.SensorDataManager()
        pass

    def readTemperature(self) -> bool:
        '''
        Method to read new data from the senseHat.
        Data is then pushed to the SensorData instance,
        then a sensorDataManager instance is called which overtakes execution.
        '''
        #Read from senseHAT     
        temp = self.sense.get_temperature()
        #Add data to sensorData
        self.sensor_data.addValue(temp)
        #Generate a will detailed string
        tempString = self.generateString()
        #Log the data and send the sensorData instance in the SensorDataManager
        logging.info(tempString)
        self.sensorDataManager.handleSensorData(self.sensor_data,tempString)
        return True   

    def generateString(self) -> str:
        '''
        Generate a detailed string from a sensorData instance and returns it.
        '''
        msgString  = "\nTemperature"
        msgString += "\n\tTime : " + self.sensor_data.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensor_data.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensor_data.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensor_data.getCount())
        msgString += "\n\tMin : " + repr(self.sensor_data.getMinValue())
        msgString += "\n\tMax : " + repr(self.sensor_data.getMaxValue())
        return msgString

        