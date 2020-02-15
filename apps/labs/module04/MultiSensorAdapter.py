'''
Created on Feb 14, 2020

@author: manik
'''
from labs.module04 import HumiditySensorAdapterTask, HI2CSensorAdapterTask, SensorDataManager
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
    
    
    def __init__(self, loop_param = 10, sleep_param = 1):
        '''
        Constructor
        '''
        print(self.LOOP_FOREVER)
        self.HumiditySensor = HumiditySensorAdapterTask.HumiditySensorAdapterTask()
        self.HI2CSensor     = HI2CSensorAdapterTask.HI2CSensorAdapterTask()
        self.dataManager    = SensorDataManager.SensorDataManager()
        self.loop_limit     = loop_param
        self.sleep_time     = sleep_param

    def __init_threads__(self):
        '''
        Initialize threads
        ''' 
        i = 0
        try:
            while i < self.loop_limit or self.LOOP_FOREVER == True:
                i = i + 1
                #Checking if HI2C Task is enabled
                if self.enableHI2CTask == True:
                    self.HI2CSensor.run()
                    i2cStr = self.HI2CSensor.generateString()
                
                #Sleeping for a small amount else we get a zero
                sleep(0.1)

                #Checking if Humidity Task is enabled
                if self.enableHumidityTask == True:
                    self.HumiditySensor.run()
                    humStr = self.HumiditySensor.generateString()

                
                
                if self.enableHI2CTask == True:
                    self.dataManager.handleSensorData(self.HI2CSensor.sensor_data,i2cStr,"HI2C")
                    sleep(self.sleep_time / 2)
                elif self.enableHumidityTask == True:
                    self.dataManager.handleSensorData(self.HumiditySensor.sensor_data,humStr,"HUM")    
                    sleep(self.sleep_time / 2)
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
        self.dataManager.SEND_EMAIL_NOTIFICATION     = self.sendEmail

        #Init and run threads
        self.__init_threads__()
 
        #Clearing after loop is done being ran.        
        self.HumiditySensor.sensorDataManager.actuatorAdapter.clear() 
        return True    
