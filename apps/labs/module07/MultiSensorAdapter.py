'''
Created on Mar 12, 2020

@author: manik
'''
from labs.module07 import TempSensorAdapterTask, CoAPClientConnector
from labs.common import PersistenceUtil
from time import sleep
import logging
import threading
import time
import os

logging.getLogger("AdapterLogger")

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdapter(object):
    '''
    Method to run TempSensorAdapterTask
    takes in sleeptime and looptime in the constructors
    has a bunch of settings to control the program behavior with 
    '''
    #Setting to ignore the looplimit set in constructor and loop forever
    LOOP_FOREVER = False
    #Enable settings
    enableTempTask = True
    enableCoAP = False
    enableRedis = False
    
    def __init__(self, loop_param = 10, sleep_param = 1):
        '''
        Constructor
        Initializing both the sensor tasks and a data manager.
        '''
        #Defining loop and sleep time
        self.loop       = loop_param
        self.sleep      = sleep_param
        #Defining CoAP Clients
        self.coAPClient = CoAPClientConnector.CoAPClientConnector()
        #Defining PersistenceUtil
        self.pUtil      = PersistenceUtil.PersistenceUtil()
        #Creating Task
        self.TempSensor = TempSensorAdapterTask.TempSensorAdapterTask(loop_param, sleep_param, self.pUtil, self.coAPClient)


    def __init_threads__(self):
        '''
        Initialize threads
        ''' 
        i = 0
        try:
            if self.enableTempTask == True:
                #Starting TempSensorAdapters thread
                self.TempSensor.start()
            #self.coAPClient.sendSensorData(self.TempSensor.sensorData)
            if self.enableRedis == True:
                self.pUtil.registerSensorDataDbmsListener()  
            else:
                logging.info("Redis Disabled")     
                
            if self.enableTempTask == False and self.enableRedis == False:
                logging.info("No thread initialized")
                return False
            while self.TempSensor.isAlive():
                sleep(0.1)
            return True
            
        #Running an event handler which checks for keyboard interrupts
        #In case of an keyboard Interrupt, this will shut down actuator and clear it
        except (KeyboardInterrupt):
            logging.info("Received keyboard interrupt.")
            self.TempSensor.stop()
            self.TempSensor.join()
            self.mqttClient.disconnect()

        return True               
        
    def runAdapter(self):
        '''
        Run method to run TempSensorAdapterTask and read temperature from the senseHAT
        '''
        i = 0
        self.TempSensor.LOOP_FOREVER = self.LOOP_FOREVER
        self.TempSensor.enableCoAP = self.enableCoAP
        #Init and run threads
        self.__init_threads__()  
        #Clearing the actuator when Task Thread stops running
        self.TempSensor.sense.clear()
        #Exiting the program
        return True
