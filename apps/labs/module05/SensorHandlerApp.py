'''
Created on Feb 14, 2020

@author: manik
'''
import threading
from labs.module05 import MultiSensorAdapter

if __name__ == '__main__':
    '''
    Creating and running a thread for Module03
    Set 'enableHumidityTask' to True to read from I2C
    Set 'enableHI2CTask' to True to read from I2C
    Set both to run them both simultaneously
    '''
    module05                    = MultiSensorAdapter.MultiSensorAdapter(1,6)                     #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    module05.enableTempTask     = True                                                           #Enable HumidityTask
    module05.enableListener     = True
    module05.LOOP_FOREVER       = True                                                         #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module05.runAdapter()