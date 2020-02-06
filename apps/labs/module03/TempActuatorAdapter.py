'''
Created on Feb 6, 2020

@author: manik
'''

class TempActuatorAdapter(object):
    '''
    Classdocs
    '''
    def __init__(self):
        self.tempAdapter = TempSensorAdapterTask()

    def updateActuator(self) -> bool: 
        pass

    def run(self):
        tempAdapter.readTemperature()
