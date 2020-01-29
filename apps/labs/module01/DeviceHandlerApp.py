'''
Created on Jan 15, 2020

@author: manik
'''
import threading
from labs.module01 import SystemPerformanceAdapter
from labs.module02 import TempEmulatorAdapter

if __name__ == '__main__':
    
    '''
    Creating and running a thread for Module01
    Set 'enableSystemPerformanceAdapter' to True to run
    '''
    sysPerfAdaptor = SystemPerformanceAdapter.SystemPerformanceAdapter(2,12)  # 2,12 refers to sleep timer and loop counter
    sysPerfAdaptor.enableSystemPerformanceAdapter = False
    sysPerfAdaptor.daemon = True
    module01_Thread = threading.Thread(target=sysPerfAdaptor.run_adapter())
    
    '''
    Creating and running a thread for Module02
    Set 'enableTempEmulatorAdapter' to True to run
    '''
    temperatureAdapter = TempEmulatorAdapter.TempEmulatorAdapter(2,12)
    temperatureAdapter.enableTempEmulatorAdapter = True
    temperatureAdapter.daemon = True
    module02_Thread = threading.Thread(target=temperatureAdapter.run_emulation())

    

