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
        Method to add new Sensor data to the class object
        '''
        self.currentValue   = var
        self.totalCount     = self.totalCount + 1
        self.totalValue     = self.totalValue + var
        self.timestamp      = str(datetime.now())
        
        if  var > self.maxValue: self.maxValue = var
        if  var < self.minValue: self.minValue = var
        
    def getAverageValue(self)  -> float:
        '''
        Method returns the average value of all the values fed to the class object
        '''
        return self.totalValue/self.totalCount 
    
    def getCount(self)         -> int:
        '''
        Method returns the total count of all the values fed to the class object
        '''
        return self.totalCount
    
    def getCurrentValue(self)  -> float:
        '''
        Method returns the last data value input 
        '''
        return self.currentValue
    
    def getMaxValue(self)      -> float:
        '''
        Method returns the maximum value seen till now
        '''
        return self.maxValue
    
    def getMinValue(self)      -> float:
        '''
        Method returns the minimum value seen till now
        '''
        return self.minValue
    
    def getName(self):
        '''
        Method returns the set name of the class object
        '''
        return self.name
    
    def setName(self,string1):
        '''
        Setter method to set the name of the current class object
        '''
        self.name = string1