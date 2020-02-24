'''
Created on Feb 21, 2020

@author: manik
'''
from labs.common import ActuatorData, SensorData, DataUtil, ActuatorDataListener, SensorDataListener
import redis
import uuid
from time import sleep
import logging
logging.getLogger("persistenceLogger")

class PersistenceUtil(object):
    '''
    Classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        connected = False
        try:
            logging.info("Connecting to redis")
            self.dataUtil             = DataUtil.DataUtil()
            #Database 0 for actuatorData JSONs
            self.redisActuator        = redis.Redis(host= "localhost", port=6379, db=0)
            self.redisActuator.ping()
            #Database 1 for sensorData JSONs
            self.redisSensor          = redis.Redis(host= "localhost", port=6379, db=1) 
            self.redisSensor.ping()
            self.connected = True
        except:
            self.connected = False
            logging.error("Could not connect to redis")


    def registerActuatorDataDbmsListener(self) -> bool:
        '''
        Register ActuatorListener to redis
        '''
        if self.connected == True:
            #Creating a thread instance of the actuatorDataListener
            actuatorDataListThread = ActuatorDataListener.ActuatorDataListener(self.redisActuator)
            #Running the thread
            actuatorDataListThread.start()
            return True
        else:
            return False    

    def registerSensorDataDbmsListener(self) -> bool:
        '''
        Register SensorListener to redis
        '''
        if self.connected == True:
            #Creating a thread instance of the sensorDataListener
            sensorDataListenerThread = SensorDataListener.SensorDataListener(self.redisSensor)
            #Running the thread
            sensorDataListenerThread.start()
            return True
        else:
            return False      

    def writeSensorDataDbmsListener(self, sensorData: SensorData.SensorData) -> bool:
        '''
        Write sensorData to redis
        '''
        if self.connected == True:
            #Convert sensorData into a JSON using DataUtil
            jsonStr = self.dataUtil.toJsonFromSensorData(sensorData)
            #Create a UUID key
            key = "sensorData-" + str(uuid.uuid4())
            #Push data to redis using key and JSON
            self.redisSensor.set(key,jsonStr)
            return True
        else:
            return False  

    def writeActuatorDataDbmsListener(self, actuatorData: ActuatorData.ActuatorData) -> bool:
        '''
        Write actuatorData to redis
        ''' 
        if self.connected == True:
            #Convert actuatorData into a JSON using DataUtil
            jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData)
            #Create a UUID key
            key = "actuatorData-" + str(uuid.uuid4())  
            #Push data to redis using key and JSON
            self.redisActuator.set(key,jsonStr)
            return True
        else:
            return False  