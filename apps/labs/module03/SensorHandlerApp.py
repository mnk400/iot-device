'''
Created on Feb 6, 2020

@author: manik
'''
import threading
from labs.module03 import TempSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module03
    Set 'enableAdapter' to True to run
    '''
    senseHATRead               = TempSensorAdapter.TempSensorAdapter(10,3)                      #10,3 refers to 10 loops with a sleep of 3 seconds
    senseHATRead.daemon        = True                                                           #Daemon yes
    senseHATRead.enableAdapter = False                                                           #Enable Adapter
    senseHATRead.sendEmail     = False                                                          #Setting to enable email notifications
    senseHATRead.LOOP_FOREVER  = False                                                          #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module03_Thread            = threading.Thread(target=senseHATRead.run_temp_adapter())       #Creating and running the thread