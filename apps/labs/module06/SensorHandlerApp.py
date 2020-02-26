'''
Created on Feb 26, 2020

@author: manik
'''
import threading
from labs.module05 import MultiSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module05
    Set 'enableTempTask' to run Temperature read thread
    Set 'enableListener to run ActuatorData Listener thread
    Set both to run them both simultaneously
    '''
    module06                    = MultiSensorAdapter.MultiSensorAdapter(1,6)                     #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    module06.enableTempTask     = True                                                           #Enable HumidityTask
    module06.enableMQTT         = True                                                           #Enable MQTT sender
    module06.LOOP_FOREVER       = True                                                           #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module06.runAdapter()