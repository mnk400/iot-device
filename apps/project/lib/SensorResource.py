'''
Created on April 5th, 2020

@author: manik
'''

class SensorResource(object):
    '''
    Singleton class, used as a shared resource
    to store some raw data read from the sensor
    and to signal the current state of the sensor.

    Does not require to use locks because only one
    class, i.e. SerialCommunicator will write to this,
    and everything else will just read
    '''
    #Store raw data for heart-rate and SPO2
    heartRate  = None
    spO2       = None
    #Store current state of the sensor
    status     = False
    #Var to store the instance of this class
    __instance = None
   
    @staticmethod 
    def getInstance():
       ''' 
       Static access method.
       '''
       if SensorResource.__instance == None:
          SensorResource()
       return SensorResource.__instance
   
    def __init__(self):
       '''
       Virtually private constructor.
       '''
       if SensorResource.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          SensorResource.__instance = self