'''
Created on Feb 21, 2020

@author: manik
'''
import redis
import threading
import logging
from time import sleep

logging.getLogger("SensorDataListenerThread")
class SensorDataListener(threading.Thread):
    '''
    Listener class which listens for SensorData Instance and then acts when data is received
    '''
    def __init__(self, rUtil: redis.Redis):
        '''
        Constructor
        '''
        #Initializing the thread
        threading.Thread.__init__(self)
        logging.info("Initializing SensorDataListenerThread")
        #assign redis object
        self.rUtil = rUtil
        #Subscribe to the notification channel waiting for new keys
        self.sensorSub = self.rUtil.pubsub()
        #'__keyspace@1__:*' is the channel new keys are broadcasted to
        self.sensorSub.psubscribe('__keyspace@1__:*')
        pass 

    def onMessage(self, key: str):
        '''
        Callback function which works when Data received
        '''
        logging.info("Received new SensorData JSON")
        print(self.rUtil.get(key))

    def listen(self):
        '''
        Function that polls and listens for new inputs on redis
        '''
        #Assigning the initial length of 
        #while True:
        self.sensorSub.get_message()
        for m in self.sensorSub.listen():
            #print(m)
            key = m['channel'].decode()
            key = key.split(':')
            self.onMessage(key[1])
                
    def run(self):
        self.listen()