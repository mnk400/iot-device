'''
Created on Jan 15, 2020

@author: manik
'''
import threading
from labs.module01 import SystemPerformanceAdapter
from labs.module02 import ConfigUtil, TempEmulatorAdapter

if __name__ == '__main__':
    
    '''
    Creating and running a thread for Module01
    '''
    sysPerfAdaptor = SystemPerformanceAdapter.SystemPerformanceAdapter(2,12)  # 2,12 refers to sleep timer and loop counter
    sysPerfAdaptor.daemon = True
    #sysPerfAdaptor.enableSystemPerformanceAdapter = True
    performance_thread = threading.Thread(target=sysPerfAdaptor.run_adapter()) 
    
    '''
    Running threads for Module02
    '''
    configEmulation = TempEmulatorAdapter.TempEmulatorAdapter()
    configEmulation.run_emulation()

    

