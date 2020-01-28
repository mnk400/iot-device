'''
Created on Jan 22, 2020

@author: manik
'''
import random
import logging
from labs.module02 import SensorData, SmtpClientConnector
from time import sleep

logging.getLogger("emulatorlog")
logging.basicConfig(format='%(message)s', level=logging.DEBUG) 
logging.info("Temperature Emulator Thread initializing")

class TempSensorEmulator():

    def __init__(self):
        '''
        Constructor
        '''
        self.sense_d    = SensorData.SensorData()
        self.minVal     = 0
        self.maxVal     = 30
        self.SmtpClient = SmtpClientConnector.MyClass()
    
    def generateData(self):
        '''
        Method to generate new random data.
        Random data is then pushed to the SensorData class
        Method also checks if newly produced data values are in the differential range of 5 from the average value
        '''     
        rand_val = random.uniform(float(self.minVal),float(self.maxVal))
        self.sense_d.addValue(rand_val)
                
        msgString= self.generateString()
        logging.info(msgString)
            
        if rand_val > self.sense_d.getAverageValue() + 5:
            self.sendNotification("Excessive Temperature\n" + msgString)
            logging.info("Excessive Temperature")
        elif rand_val < self.sense_d.getAverageValue() - 5:
            self.sendNotification("Temperature too low\n" + msgString)
            logging.info("Temperature too low")
                
        
    def getSensorData(self) -> SensorData.SensorData:
        '''
        Returns an instance of the the class SensorData
        '''
        return self.sense_d
    
    def sendNotification(self,message_param):
        '''
        Simple method to call the SMTP connector to publish a message
        '''
        self.SmtpClient.publishMessage("IOT-Deivce", message_param)
        logging.info("Sending E-mail")
        
    def generateString(self) -> str:
        '''
        Generate the string to be logged and then passed in the SMTP message
        '''
        msgString  = "\nTemperature"
        msgString += "\n\tTime : " + self.sense_d.timestamp
        msgString += "\n\tCurrent : " + repr(self.sense_d.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sense_d.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sense_d.getCount())
        msgString += "\n\tMin : " + repr(self.sense_d.getMinValue())
        msgString += "\n\tMax : " + repr(self.sense_d.getMaxValue())
        return msgString