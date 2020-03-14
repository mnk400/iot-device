'''
Created on Mar 12, 2020

@author: manik
'''

import threading
from labs.module07 import MultiSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module05
    Set 'enableTempTask' to run Temperature read thread
    Set 'enableListener to run ActuatorData Listener thread
    Set both to run them both simultaneously
    '''
    module07                    = MultiSensorAdapter.MultiSensorAdapter(1,6)                     #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    module07.enableTempTask     = True                                                           #Enable HumidityTask
    module07.enableCoAP         = True                                                           #Enable MQTT sender
    module07.enableRedis        = False                                                          #Enable Redis Database
    module07.LOOP_FOREVER       = True                                                           #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module07.runAdapter()