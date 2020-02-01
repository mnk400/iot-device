'''
Created on Jan 22, 2020

@author: manik
'''
import threading
from labs.module02 import TempSensorEmulatorTask
from time import sleep
import logging

logging.getLogger("adapterlog")
class TempEmulatorAdapter(object):
    '''
    This class is responsible for running the temperature generation emulator
    Has inputs like the sleeptimer and looplimit so we can control the running of iterations
    '''
    #enableTempEmulatorAdapter to run the thread and generate Data
    enableTempEmulatorAdapter = False
    sleepDefault = 1
    loopDefault = 0
    
    def __init__(self,sleep_param = sleepDefault,looplimit = loopDefault):
        '''
        Constructor
        which sets the sleep timer for the thread, and a looplimit if needed.
        '''
        self.sleeptime       = sleep_param
        self.looplimit       = looplimit
        self.temperatureTask = TempSensorEmulatorTask.TempSensorEmulator()
    
        
    def run_emulation(self):
        '''
        This method runs the emulation if enableTempEmulatorAdapter is set to True.
        Method calls the "generateData" method from the tempEmulatorAdapter which is
        responsible for emulator a temperature Data generator.
        '''
        i = 0
        #return false if sleeptime or looplimit is less than 0 and log
        if self.sleeptime < 0 or self.looplimit < 0:
            logging.error("looplimit or sleeptime is less than 0")
            return False

        #run if enableTempEmulator is true
        if self.enableTempEmulatorAdapter == True:
            while i < self.looplimit:
                i = i + 1
                #call generateData method
                self.temperatureTask.generateData()
                sleep(self.sleeptime)
            #return true if ran correctly    
            return True 
        #return false if enableTempEmulator was false    
        return False           