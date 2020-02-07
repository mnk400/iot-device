'''
Created on Feb 6, 2020

@author: manik
'''
from threading import Thread
from labs.module03 import TempSensorAdapter
import logging
logging.getLogger("hello")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
if __name__ == '__main__':
    '''
    Creating and running a thread for Module03
    Set 'enableTempEmulatorAdapter' to True to run
    '''
    senseHATRead = TempSensorAdapter.TempSensorAdapter()
    senseHATRead.run()