'''
Created on April 5th, 2020

@author: manik
'''

class sensorResource(object):
    
    heartRate  = None
    spO2       = None
    status     = False
    __instance = None
   
    @staticmethod 
    def getInstance():
       """ Static access method. """
       if sensorResource.__instance == None:
          sensorResource()
       return sensorResource.__instance
   
    def __init__(self):
       """ Virtually private constructor. """
       if sensorResource.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          sensorResource.__instance = self