'''
Created on Feb 21, 2020

@author: manik
'''

class PersistenceUtil(object):
    '''
    Classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass

    def registerActuatorDataDbmsListener(self) -> bool:
        '''
        Register ActuatorListener to redis
        '''
        pass

    def registerSensorDataDbmsListener(self) -> bool:
        '''
        Register SensorListener to redis
        '''
        pass

    def writeSensorDataDbmsListener(self, sensorData) -> bool:
        '''
        Write sensorData to redis
        '''
        pass 

    def writeActuatorDataDbmsListener(self, actuatorData) -> bool:
        '''
        Write actuatorData to redis
        '''
        pass 

    