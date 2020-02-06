'''
Created on Feb 6, 2020

@author: manik
'''
import logging
from sense_hat import SenseHat
logging.getLogger("tempReaderLogger")

class TempSensorAdapterTask(object):
    '''
    Classdocs
    '''
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        pass

    def readTemperature(self):
        '''
        Method to read new data from the senseHat.
        Random data is then pushed to the SensorData class
        Method also checks if newly produced data values are in the differential range of a set threshold from the set value, otherwise call a notification.
        '''     
        #temp = self.sense.get_temperature()
        #self.sensor.addValue(value)
        #logging.info(temp)
        self.sense.show_message("this message here")
        return True   