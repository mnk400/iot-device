'''
Created on Feb 21, 2020

@author: manik
'''
from labs.common import ActuatorData, SensorData, DataUtil, ActuatorDataListener, SensorDataListener
import redis
import uuid
from time import sleep

class PersistenceUtil(object):
    '''
    Classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.dataUtil             = DataUtil.DataUtil()
        #Database 0 for actuatorData JSONs
        self.redisActuator        = redis.Redis(host= "localhost", port=6379, db=0)
        #Database 1 for sensorData JSONs
        self.redisSensor          = redis.Redis(host= "localhost", port=6379, db=1)

    def registerActuatorDataDbmsListener(self) -> bool:
        '''
        Register ActuatorListener to redis
        '''
        #Creating a thread instance of the actuatorDataListener
        actuatorDataListThread = ActuatorDataListener.ActuatorDataListener(self.redisActuator)
        #Running the thread
        actuatorDataListThread.start()
        return True

    def registerSensorDataDbmsListener(self) -> bool:
        '''
        Register SensorListener to redis
        '''
        #Creating a thread instance of the sensorDataListener
        sensorDataListenerThread = SensorDataListener.SensorDataListener(self.redisSensor)
        #Running the thread
        sensorDataListenerThread.start()
        return True

    def writeSensorDataDbmsListener(self, sensorData: SensorData.SensorData) -> bool:
        '''
        Write sensorData to redis
        '''
        #Convert sensorData into a JSON using DataUtil
        jsonStr = self.dataUtil.toJsonFromSensorData(sensorData)
        #Create a UUID key
        key = "sensorData-" + str(uuid.uuid4())
        #Push data to redis using key and JSON
        self.redisSensor.set(key,jsonStr)
        return True

    def writeActuatorDataDbmsListener(self, actuatorData: ActuatorData.ActuatorData) -> bool:
        '''
        Write actuatorData to redis
        ''' 
        #Convert actuatorData into a JSON using DataUtil
        jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData)
        #Create a UUID key
        key = "actuatorData-" + str(uuid.uuid4())  
        #Push data to redis using key and JSON
        self.redisActuator.set(key,jsonStr)
        return True