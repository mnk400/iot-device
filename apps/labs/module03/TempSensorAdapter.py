'''
Created on Feb 6, 2020

@author: manik
'''
from labs.module03 import TempSensorAdapterTask
from time import sleep
import logging

logging.getLogger("TempSensorAdapterLogger")
logging.info("TempSensorAdapter thread Initializing")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class TempSensorAdapter(object):
    '''
    Method to run TempSensorAdapterTask
    takes in sleeptime and looptime in the constructor
    has a bunch of settings to control the program behavior with 
    '''
    #Setting to ignore the looplimit set in constructor and loop forever
    LOOP_FOREVER = False
    #Setting to enable sending emails as notifications, this variable sets the SEND_EMAIL_NOTIFICATION variable in SensorDataManager 
    sendEmail = True
    #Enable setting
    enableAdapter = True
    
    def __init__(self, loop_param = 1, sleep_param = 3):
        '''
        Constructor
        '''
        self.TempSensor = TempSensorAdapterTask.TempSensorAdapterTask()
        self.looplimit = loop_param
        self.sleeptime = sleep_param

    def run_temp_adapter(self) -> bool:
        '''
        Run method to run TempSensorAdapterTask and read temperature from the senseHAT
        '''
        i = 0
        #Setting the variable in SensorDataManager
        self.TempSensor.sensorDataManager.SEND_EMAIL_NOTIFICATION = self.sendEmail
        #Return false if enableAdapter is not set
        if self.enableAdapter == False:
            return False
        #Check against looplimit or the LOOP_FOREVER setting    
        while i < self.looplimit or self.LOOP_FOREVER == True:
            i = i + 1
            #In try catch block to check for keyboard interrupt
            try:
                self.TempSensor.readTemperature()
                sleep(self.sleeptime)
            except KeyboardInterrupt:
                #If Keyboard interrupt occours, clears the LED matrix on SenseHAT
                #Random keyboard interrupt can lead to LED matrix on all the time 
                #Which then you'd have to manually go in and clear
                logging.info("Keyboard Interrupt: Shutting Actuator Down")
                #calling the clear function in TempActuatorAdapter and exiting
                self.TempSensor.sensorDataManager.actuatorAdapter.clear()
                exit()     
        #Clearing after loop is done being ran.        
        self.TempSensor.sensorDataManager.actuatorAdapter.clear()  
        return True    
