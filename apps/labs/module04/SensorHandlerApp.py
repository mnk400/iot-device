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
    i2cRead                    = MultiSensorAdapter.MultiSensorAdapter(1,8)                 #Looptime and sleeptime of humidityTask and HI2CTask respectivley
    i2cRead.daemon             = True
    i2cRead.enableHumidityTask = True                                                           #Enable HumidityTask
    i2cRead.enableHI2CTask     = True                                                           #Enable HI2CTask
    i2cRead.sendEmail          = False                                                         #Setting to enable email notifications
    i2cRead.LOOP_FOREVER       = True                                                         #Loop forever setting, if yes, program ignores the loopvalue set in the constructor
    module04_Thread            = threading.Thread(target=i2cRead.runAdapter())