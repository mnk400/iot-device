'''
Created on Feb 14, 2020

@author: manik
'''
from labs.module04 import HumiditySensorAdapterTask, HI2CSensorAdapterTask
from time import sleep
import logging

logging.getLogger("AdapterLogger")
logging.info("SensorAdapter thread Initializing")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdapter(object):
    '''
    Method to run TempSensorAdapterTask
    takes in sleeptime and looptime in the constructor
    has a bunch of settings to control the program behavior with 
    '''
    #Setting to ignore the looplimit set in constructor and loop forever
    LOOP_FOREVER = False
    #Setting to enable sending emails as notifications, this variable sets the SEND_EMAIL_NOTIFICATION variable in SensorDataManager 
    sendEmail = True
    #Enable settings
    enableHumidityTask = True
    enableHI2CTask = True
    
    def __init__(self, loop_param = 1, sleep_param = 3):
        '''
        Constructor
        '''
        self.HumiditySensor = HumiditySensorAdapterTask.HumiditySensorAdapterTask()
        self.HI2CSensor  = HI2CSensorAdapterTask.HI2CSensorAdapterTask()
        self.looplimit = loop_param
        self.sleeptime = sleep_param

    def run_temp_adapter(self) -> bool:
        '''
        Run method to run TempSensorAdapterTask and read temperature from the senseHAT
        '''
        i = 0
        #Setting the variable in SensorDataManager
        #self.HI2CSensor.sensorDataManager.SEND_EMAIL_NOTIFICATION = self.sendEmail
    
        #Check against looplimit or the LOOP_FOREVER setting    
        while i < self.looplimit or self.LOOP_FOREVER == True:
            i = i + 1
            #In try catch block to check for keyboard interrupt
            try:
                self.HumiditySensor.readTemperature()
                sleep(self.sleeptime)
            except KeyboardInterrupt:
                #If Keyboard interrupt occours, clears the LED matrix on SenseHAT
                #Random keyboard interrupt can lead to LED matrix on all the time 
                #Which then you'd have to manually go in and clear
                logging.info("Keyboard Interrupt: Shutting Actuator Down")
                #calling the clear function in TempActuatorAdapter and exiting
                self.HumiditySensor.sensorDataManager.actuatorAdapter.clear()
                exit()     
        #Clearing after loop is done being ran.        
        self.HumiditySensor.sensorDataManager.actuatorAdapter.clear()  
        return True    
