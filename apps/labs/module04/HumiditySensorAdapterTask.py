'''
Created on Feb 14, 2020

@author: manik
'''
import logging
import threading
from labs.common import SensorData
from sense_hat import SenseHat
from labs.module04 import SensorDataManager
from time import sleep

logging.getLogger("tempReaderLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class HumiditySensorAdapterTask(threading.Thread):
    '''
    Class which reads the temperature data from the SenseHAT.
    Stores the data in the SensorData class and then further
    calls SensorDataManager to parse the stored data.
    '''

    loopforever = False
    def __init__(self, loop_param, sleep_param):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)

        #Creating a SensorData instance and setting it's name
        self.sensor_data = SensorData.SensorData()
        self.sensor_data.setName("Temperature Sensor Data")

        #SenseHat instance to interact with the senseHAT
        self.sense = SenseHat()

        #clearing matrix
        self.sense.clear()

        #SensorDataManager instance
        self.sensorDataManager = SensorDataManager.SensorDataManager()

        #Setting looplimit and sleeptime 
        self.looplimit = loop_param
        self.sleeptime = sleep_param
        pass

    def run(self):
        '''
        Method to read new data from the senseHat.
        Data is then pushed to the SensorData instance,
        then a sensorDataManager instance is called which overtakes execution.
        '''
        i=0
        while i < self.looplimit or self.loopforever == True:
            i = i + 1

            #Read from senseHAT     
            humData = self.sense.get_humidity()

            #Add data to sensorData
            self.sensor_data.addValue(humData)

            #Generate a will detailed string
            humString = self.generateString()

            #Log the data and send the sensorData instance in the SensorDataManager
            logging.info(humString)
            self.sensorDataManager.handleSensorData(self.sensor_data,humString)
            sleep(self.sleeptime)

        self.sensorDataManager.actuatorAdapter.clear()    
        return True 

    def generateString(self) -> str:
        '''
        Generate a detailed string from a sensorData instance and returns it.
        '''
        msgString  = "\nHumidity from the sense_HAT API:"
        msgString += "\n\tTime : " + self.sensor_data.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensor_data.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensor_data.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensor_data.getCount())
        msgString += "\n\tMin : " + repr(self.sensor_data.getMinValue())
        msgString += "\n\tMax : " + repr(self.sensor_data.getMaxValue())
        return msgString

        