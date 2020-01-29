'''
Created on Jan 22, 2020

@author: manik
'''
import threading
from labs.module02 import TempSensorEmulatorTask
from time import sleep

class TempEmulatorAdapter(object):

    enableTempEmulatorAdapter = False
    sleepDefault = 1
    loopDefault = 1
    
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
        if self.sleeptime < 0 or self.looplimit < 0:
            return False

        if self.enableTempEmulatorAdapter == True:
            while i < self.looplimit:
                i = i + 1
                self.temperatureTask.generateData()
                sleep(self.sleeptime)
            return True 
        return False           