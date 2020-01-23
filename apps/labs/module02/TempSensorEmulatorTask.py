'''
Created on Jan 22, 2020

@author: manik
'''
import random
import logging
from labs.module02 import SensorData
from time import sleep

logging.getLogger("emulatorlog")
logging.basicConfig(format='%(message)s', level=logging.DEBUG) 
logging.info("Temperature Emulator Thread initializing")

class TempSensorEmulator():
    '''
    classdocs
    '''
    enableDataGenerator = False
    
    def __init__(self,sleepparam,looplimit):
        '''
        Constructor
        '''
        self.sense_d    = SensorData.SensorData()
        self.minVal     = 0
        self.maxVal     = 30
        self.sleeptime  = sleepparam
        self.looplimit  = looplimit
    
    def generateData(self):
        i = 0
        while i < self.looplimit:
            i = i + 1
            if self.enableDataGenerator == True:
                rand_val = random.uniform(float(self.minVal),float(self.maxVal))
                self.sense_d.addValue(rand_val)
            
            if rand_val > self.sense_d.getAverageValue() + 5:
                self.sendNotification("Excessive Temperature")
            elif rand_val < self.sense_d.getAverageValue() - 5:
                self.sendNotification("Temperature too low")
        
            logging.info("Temperature : ")    
            #logging.info("Time : " + repr(self.sense_d.timestamp))
            logging.info("Current : " + repr(self.sense_d.getCurrentValue()))
            logging.info("Average : " + repr(self.sense_d.getAverageValue()))
            logging.info("Samples : " + repr(self.sense_d.getCount()))
            logging.info("Min : " + repr(self.sense_d.getMinValue()))
            logging.info("Max : " + repr(self.sense_d.getMaxValue()))  
            sleep(self.sleeptime)
                
        
    def getSensorData(self) -> SensorData.SensorData:
        return self.sense_d
    
    def sendNotification(self,message_param):
        print(message_param)
    