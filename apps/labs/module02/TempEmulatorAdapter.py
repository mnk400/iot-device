'''
Created on Jan 22, 2020

@author: manik
'''
import threading
from labs.module02 import TempSensorEmulatorTask
from time import sleep

class TempEmulatorAdapter(object):

    enableTempEmulatorAdapter = False
    
    def __init__(self,sleepparam,looplimit):
        '''
        Constructor
        '''
        self.sleeptime  = sleepparam
        self.looplimit  = looplimit
        self.temperatureTask = TempSensorEmulatorTask.TempSensorEmulator()
        
    def run_emulation(self):
        '''
        This method runs the emulation if enableTempEmulatorAdapter is set to True
        '''
        i = 0
        if self.enableTempEmulatorAdapter == True:
            while i < self.looplimit:
                i = i + 1
                self.temperatureTask.generateData()
                sleep(self.sleeptime)
            