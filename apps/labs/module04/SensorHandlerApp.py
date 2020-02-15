'''
Created on Feb 14, 2020

@author: manik
'''
import threading
from labs.module04 import MultiSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module03
    Set 'enableAdapter' to True to run
    '''
    senseHATRead                    = MultiSensorAdapter.MultiSensorAdapter(1,3,1,3)            #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    senseHATRead.enableHumidityTask = True                                                           #Enable HumidityTask
    senseHATRead.enableHI2CTask     = True                                                           #Enable HI2CTask
    senseHATRead.sendEmail          = False                                                          #Setting to enable email notifications
    senseHATRead.LOOP_FOREVER       = False                                                          #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    senseHATRead.runAdapter()