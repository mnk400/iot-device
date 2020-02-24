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
        try:
            #assign redis object
            self.rUtil = rUtil
            #Subscribe to the notification channel waiting for new keys
            self.actuatorSub = self.rUtil.pubsub()
            #'__keyspace@0__:*' is the channel new keys are broadcasted to
            self.actuatorSub.psubscribe('__keyspace@0__:*')
            self.connected = True
        except:
            self.connected = False
            logging.error("Could not connect to redis:ActuatorDataListener")
        #ActuatorAdapter instance
        self.actuatorAdapter = MultiActuatorAdapter.MultiActuatorAdapter()
        #Creating a DataUtil instance
        self.dataUtil = DataUtil.DataUtil()
        pass 

    def onMessage(self, tempActuator) -> bool:
        '''
        Callback function which works when Data received
        '''
        logging.info("Received new ActuatorData JSON, Actuating")
        self.actuatorAdapter.updateActuator(tempActuator)
        return True

 
    def listen(self):
        '''
        Subscribes to redis channel and listens for new messages
        '''
        self.actuatorSub.get_message()
        if self.connected = True:
            for m in self.actuatorSub.listen():
                key = m['channel'].decode()
                key = key.split(':')
                tempActuator = self.dataUtil.toActuatorDataFromJson(self.rUtil.get(key[1]))
                self.onMessage(tempActuator)
        else:
            return False          

    def run(self):
        '''
        Thread run, call listen()
        '''
        self.listen()        