'''
Created on Feb 21, 2020

@author: manik
'''

class DataUtil(object):
    '''
    Class to handle JSON data,
    convert from JSON to sensorData or actuatorData instance
    or convert sensorData or actuatorDat instance to JSON.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def toJsonFromSensorData(self):
        '''
        Convert from JSON to SensorData instance
        '''
        pass

    def toSensorDataFromJson(self):
        '''
        Convert from SensorData instance to JSON
        '''
        pass    
    
    def writeSensorDataToFile(self, SensorData):
        '''
        Converts SensorData to JSON and writes to the filesystem
        '''
        pass

    def toJsonFromActuatorData(self):
        '''
        Convert from JSON to ActuatorData instance
        '''
        pass

    def toActuatorDataFromJson(self):
        '''
        Convert from ActuatorData instance to JSON
        '''
        pass    
    
    def writeActuatorDataToFile(self, SensorData):
        '''
        Converts ActuatorData to JSON and writes to the filesystem
        '''
        pass
