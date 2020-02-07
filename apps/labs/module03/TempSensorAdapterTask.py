'''
Created on Feb 6, 2020

@author: manik
'''
import logging
from labs.common import SensorData
from sense_hat import SenseHat
from labs.module03 import SensorDataManager
logging.getLogger("tempReaderLogger")

class TempSensorAdapterTask(object):
    '''
    Classdocs
    '''

    def __init__(self):
        self.sensor_data = SensorData.SensorData()
        self.sensor_data.setName("Temperature Sensor Data")
        self.sense = SenseHat()
        self.sense.clear()
        self.sensorDataManager = SensorDataManager.SensorDataManager()
        pass

    def readTemperature(self):
        '''
        Method to read new data from the senseHat.
        Random data is then pushed to the SensorData class
        Method also checks if newly produced data values are in the differential range of a set threshold from the set value, otherwise call a notification.
        '''     
        temp = self.sense.get_temperature()
        self.sensor_data.addValue(temp)
        tempString = self.generateString()
        logging.info(tempString)
        self.sensorDataManager.handleSensorData(self.sensor_data)
        return True   

    def generateString(self) -> str:
        '''
        Generate the string to be logged and then passed in the SMTP message
        '''
        msgString  = "\nTemperature"
        msgString += "\n\tTime : " + self.sensor_data.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensor_data.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensor_data.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensor_data.getCount())
        msgString += "\n\tMin : " + repr(self.sensor_data.getMinValue())
        msgString += "\n\tMax : " + repr(self.sensor_data.getMaxValue())
        return msgString

        