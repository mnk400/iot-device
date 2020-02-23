'''
Created on Feb 21, 2020

@author: manik
'''
import threading
import redis
import logging
from labs.common import DataUtil, ActuatorData
from time import sleep
from labs.module05 import MultiActuatorAdapter

logging.getLogger("ActuatorDataListenerThread")
class ActuatorDataListener(threading.Thread):
    '''
    Listener class which listens for ActuatorData Instance and then acts when data is received
    '''
    def __init__(self, rUtil: redis.Redis):
        '''
        Constructor
        '''
        #Initializing the thread
        threading.Thread.__init__(self)
        logging.info("Initializing ActuatorDataListenerThread")
        #assign redis object
        self.rUtil = rUtil
        #Subscribe to the notification channel waiting for new keys
        self.actuatorSub = self.rUtil.pubsub()
        #'__keyspace@0__:*' is the channel new keys are broadcasted to
        self.actuatorSub.psubscribe('__keyspace@0__:*')
        #ActuatorAdapter instance
        self.actuatorAdapter = MultiActuatorAdapter.MultiActuatorAdapter()
        #Creating a DataUtil instance
        self.dataUtil = DataUtil.DataUtil()
        pass 

    def onMessage(self, key: str):
        '''
        Callback function which works when Data received
        '''
        logging.info("Received new ActuatorData JSON, Actuating")
        tempActuator = self.dataUtil.toActuatorDataFromJson(self.rUtil.get(key))
        self.actuatorAdapter.updateActuator(tempActuator)

 
    def listen(self):
        '''
        Subscribes to redis channel and listens for new messages
        '''
        self.actuatorSub.get_message()
        for m in self.actuatorSub.listen():
            key = m['channel'].decode()
            key = key.split(':')
            self.onMessage(key[1])
                  

    def run(self):
        self.listen()        