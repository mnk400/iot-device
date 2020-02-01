'''
Created on Jan 22, 2020

@author: manik
'''
from datetime import datetime
import string
import logging
logging.getLogger("SensorDataLogger")   #Get a logger instance

class SensorData(object):
    '''
    Class to store the sensor data being recording from a sensor
    contains certain variables such as average, minimum and maximum
    '''
    def __init__(self):
        '''
        Constructor
        Defines some class variables we'll be using to store our data in
        and then initializing the variables
        '''
        self.currentValue   = float(0.0)
        self.totalCount     = float(0.0)
        self.totalValue     = float(0.0)
        self.maxValue       = float(-99.99)
        self.minValue       = float(99.99)
        self.name           = "Not Set"
        self.timestamp      = None
        
    def addValue(self,var):
        '''
        Method to add new Sensor data to the class object
        '''
        try:
            #In a try block just in case a wrong datatype gets passed
            #Logging the data in our class variables
            #Calculating and updating values like averages/min/max as new data is input
            self.currentValue   = float(var)
            self.totalCount     = self.totalCount + 1
            self.totalValue     = self.totalValue + var
            self.timestamp      = str(datetime.now())
        
            if  var > self.maxValue: self.maxValue = var
            if  var < self.minValue: self.minValue = var

        except Exception as e:
            #returns a false if an exception occurs and logging event
            logging.error(e)
            return False
        #returns true if method worked properly    
        return True
        
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