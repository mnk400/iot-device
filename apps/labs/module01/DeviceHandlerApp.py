'''
Created on Jan 15, 2020

@author: manik
'''
import threading
from labs.module01 import SystemPerformanceAdapter

if __name__ == '__main__':
    '''
    Creating a thread for the SystemPerformanceAdapter
    '''
    sysPerfAdaptor = SystemPerformanceAdapter.SystemPerformanceAdapter(2) 
    sysPerfAdaptor.daemon = True
    performance_thread = threading.Thread(target=sysPerfAdaptor.run(12))
    performance_thread.start()