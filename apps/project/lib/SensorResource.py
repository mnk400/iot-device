'''
Created on April 5th, 2020

@author: manik
'''

class SensorResource(object):
    
    heartRate  = None
    spO2       = None
    status     = False
    __instance = None
   
    @staticmethod 
    def getInstance():
       """ Static access method. """
       if SensorResource.__instance == None:
          SensorResource()
       return SensorResource.__instance
   
    def __init__(self):
       """ Virtually private constructor. """
       if SensorResource.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          SensorResource.__instance = self