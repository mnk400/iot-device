'''
Created on Feb 14, 2020

@author: manik
'''
from labs.module04 import HumiditySensorAdapterTask, HI2CSensorAdapterTask
from time import sleep
import logging
import threading
import sys
import time

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
    #Setting to enable sending emails as notifications, this variable sets the SEND_EMAIL_NOTIFICATION variable in SensorDataManager 
    sendEmail = True
    #Enable settings
    enableHumidityTask = True
    enableHI2CTask = True
    
    def __init__(self, loop_param_hum = 10, sleep_param_hum = 3, loop_param_i2c = 10, sleep_param_i2c = 3):
        '''
        Constructor
        '''
        print(self.LOOP_FOREVER)
        self.HumiditySensor = HumiditySensorAdapterTask.HumiditySensorAdapterTask(loop_param_hum, sleep_param_hum)
        self.HI2CSensor  = HI2CSensorAdapterTask.HI2CSensorAdapterTask(loop_param_i2c, sleep_param_i2c)

    def __init_threads__(self):
        '''
        Initialize threads
        ''' 
        
        try:
            #Running humidity from senseHAT API Thread if enabled
            if self.enableHumidityTask == True:
                logging.info("HumiditySensorAdapterTask initialized")
                self.HumiditySensor.daemon = True
                self.HumiditySensor.start()
                
            #Running I2C thread if enabled
            if self.enableHI2CTask == True:  
                logging.info("HI2CSensorAdapterTask initialized")
                self.HI2CSensor.daemon = True  
                self.HI2CSensor.start()

            #Polling if threads are alive so we can shut the actuator down after they die.
            while self.HumiditySensor.isAlive() or self.HI2CSensor.isAlive(): 
                time.sleep(1)
        #Running an event handler which checks for keyboard interrupts
        #In case of an keyboard Interrupt, this will shut down actuator and clear it
        except (KeyboardInterrupt):
                logging.info("Received keyboard interrupt, quitting threads.\n")
                self.HumiditySensor.sensorDataManager.actuatorAdapter.clear()
                return True

        #Logging if none of them initialized
        if self.enableHI2CTask == False and self.enableHumidityTask == False:
            logging.info("No thread initialized")  

        return True               
        
    def runAdapter(self) -> bool:
        '''
        Run method to run TempSensorAdapterTask and read temperature from the senseHAT
        '''
        i = 0

        #Setting the sendEmail variable in SensorDataManagers
        self.HI2CSensor.sensorDataManager.SEND_EMAIL_NOTIFICATION     = self.sendEmail
        self.HumiditySensor.sensorDataManager.SEND_EMAIL_NOTIFICATION = self.sendEmail

        #Setting loopforever variables 
        self.HI2CSensor.loopforever     = self.LOOP_FOREVER
        self.HumiditySensor.loopforever = self.LOOP_FOREVER

        #Init and run threads
        self.__init_threads__()
 
        #Clearing after loop is done being ran.        
        self.HumiditySensor.sensorDataManager.actuatorAdapter.clear() 
        return True    
