'''
Created on Feb 14, 2020

@author: manik
'''
from labs.module05 import HumiditySensorAdapterTask, HI2CSensorAdapterTask, SensorDataManager
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
        Initializing both the sensor tasks and a data manager.
        '''
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

                diff = abs(self.HI2CSensor.sensor_data.getCurrentValue() - self.HumiditySensor.sensor_data.getCurrentValue())
                logging.info("Difference between the two values is: " + str(diff))
                #Checking again what tasks were enabled so we can call HandleSensorData
                #and hence perform some actuation
                #
                #HandleSensorData wasn't called previously because we wanted to capture the data 
                #from both the ways as close to each other in time as possible so we could get 
                #really small differences
                #
                #Now, in the sleep timing between two reads, actuator time is divided equally among 
                #the both readings, HI2C displays the floor of it's value in red for sleeptime/2 seconds 
                #and HUM displays the floor of it's value in red for sleeptime/2 seconds
                if self.enableHI2CTask == True:
                    self.dataManager.handleSensorData(self.HI2CSensor.sensor_data,i2cStr,"HI2C")
                    sleep(self.sleep_time / 2)
                if self.enableHumidityTask == True:
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
