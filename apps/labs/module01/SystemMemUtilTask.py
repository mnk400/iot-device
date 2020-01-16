'''
Created on Jan 15, 2020

@author: manik
'''
import psutil

class Mem(object):

    def __init__(self):
        '''
        Constructor
        '''
        
    def getDataFromSensor(self):
        '''
        Method to return percentage of system memory being used
        '''
        return psutil.virtual_memory()[2]