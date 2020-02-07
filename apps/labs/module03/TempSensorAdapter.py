'''
Created on Feb 6, 2020

@author: manik
'''
from labs.module03 import TempSensorAdapterTask
from time import sleep

class TempSensorAdapter(object):
    
    def __init__(self):
        self.TempSensor = TempSensorAdapterTask.TempSensorAdapterTask()
        self.looplimit = 1

    def run(self):
        i = 0
        while i < self.looplimit:
            i = i + 1
            self.TempSensor.readTemperature()
