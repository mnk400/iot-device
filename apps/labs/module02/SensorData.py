'''
Created on Jan 22, 2020

@author: manik
'''
from datetime import datetime
import string

class SensorData(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.currentValue   = float(0.0)
        self.averageValue   = float(0.0)
        self.totalCount     = float(0.0)
        self.totalValue     = float(0.0)
        self.maxValue       = float(-99.99)
        self.minValue       = float(99.99)
        self.name           = ""
        self.timestamp      = None
        
    def addValue(self,var):
        '''
        Method to add new Sensor data
        '''
        self.currentValue   = var
        self.totalCount     = self.totalCount + 1
        self.totalValue     = self.totalValue + var
        self.timestamp      = str(datetime.now())
        
        if  var > self.maxValue: self.maxValue = var
        if  var < self.minValue: self.minValue = var
        
    def getAverageValue(self)  -> float:
        return self.totalValue/self.totalCount 
    
    def getCount(self)         -> int:
        return self.totalCount
    
    def getCurrentValue(self)  -> float:
        return self.currentValue
    
    def getMaxValue(self)      -> float:
        return self.maxValue
    
    def getMinValue(self)      -> float:
        return self.minValue
    
    def getName(self):
        return self.name
    
    def setName(self,string1):
        self.name = string1