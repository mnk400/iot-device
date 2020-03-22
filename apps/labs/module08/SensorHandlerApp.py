'''
Created on Mar 21, 2020

@author: manik
'''

import threading
from labs.module08 import MultiSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module05
    Set 'enableTempTask' to run Temperature read thread
    Set 'enableListener to run ActuatorData Listener thread
    Set both to run them both simultaneously
    '''
    module08                        = MultiSensorAdapter.MultiSensorAdapter(1,6)                     #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    module08.enableTempTask         = True                                                           #Enable HumidityTask
    module08.enableMQTT             = True                                                           #Enable MQTT sender
    module08.enableActuatorListener = True
    module08.enableRedis            = False                                                          #Enable Redis Database
    module08.LOOP_FOREVER           = True                                                           #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module08.runAdapter()