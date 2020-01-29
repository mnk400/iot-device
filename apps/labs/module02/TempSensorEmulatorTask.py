'''
Created on Jan 22, 2020

@author: manik
'''
import random
import logging
from labs.module02 import  SmtpClientConnector
from labs.common import SensorData
from time import sleep

logging.getLogger("emulatorlog")
logging.basicConfig(format='%(message)s', level=logging.DEBUG) 
logging.info("Temperature Emulator Thread initializing")

class TempSensorEmulator():

    minVal = 0
    maxVal = 30
    threshold = 5
    topic = "IOT - Device"

    def __init__(self):
        '''
        Constructor
        '''
        self.sensor    = SensorData.SensorData()
        self.SmtpClient = SmtpClientConnector.MyClass()
    
    def generateData(self):
        '''
        Method to generate new random data.
        Random data is then pushed to the SensorData class
        Method also checks if newly produced data values are in the differential range of 5 from the average value
        '''     
        rand_val = random.uniform(float(self.minVal),float(self.maxVal))
        self.sensor.addValue(rand_val)
                
        msgString= self.generateString()
        logging.info(msgString)
            
        if rand_val > self.sensor.getAverageValue() + self.threshold or rand_val < self.sensor.getAverageValue() - self.threshold:
            logging.info("Temperature out of bounds")
            self.sendNotification("Temperature out of bounds\n" + msgString)
        
        return True   
                
        
    def getSensorData(self) -> SensorData.SensorData:
        '''
        Returns an instance of the the class SensorData
        '''
        return self.sensor
    
    def sendNotification(self,message_param):
        '''
        Simple method to call the SMTP connector to publish a message
        '''
        logging.info("Sending Notification")
        self.SmtpClient.publishMessage(self.topic, message_param)
        
        
    def generateString(self) -> str:
        '''
        Generate the string to be logged and then passed in the SMTP message
        '''
        msgString  = "\nTemperature"
        msgString += "\n\tTime : " + self.sensor.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensor.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensor.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensor.getCount())
        msgString += "\n\tMin : " + repr(self.sensor.getMinValue())
        msgString += "\n\tMax : " + repr(self.sensor.getMaxValue())
        return msgString