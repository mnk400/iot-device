'''
Created on Jan 22, 2020

@author: manik
'''
import threading
from labs.module02 import TempSensorEmulatorTask

class TempEmulatorAdapter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def run_emulation(self):
        emulator_obj = TempSensorEmulatorTask.TempSensorEmulator(3,10)
        emulator_obj.enableDataGenerator = True
        emulator_obj.daemon = True
        generator_thread = threading.Thread(target=emulator_obj.generateData())



        