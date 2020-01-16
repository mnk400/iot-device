'''
Created on Jan 15, 2020

@author: manik
'''
import psutil

class Cpu(object):

    def __init__(self):
        '''
        Constructor
        '''
        
    def getDataFromSensor(self):
        '''
        Method to return percentage of CPU being used
        '''
        return psutil.cpu_percent(interval=1)