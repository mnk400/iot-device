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
        pass

    def readTemperature(self):
        '''
        Method to read new data from the senseHat.
        Random data is then pushed to the SensorData class
        Method also checks if newly produced data values are in the differential range of a set threshold from the set value, otherwise call a notification.
        '''     
        rand_val = random.uniform(float(self.minVal),float(self.maxVal))
        self.sensor.addValue(rand_val)
        #Generating string containing all the data points for sending email and logging         
        msgString= self.generateString()
        logging.info(msgString)
        return True   