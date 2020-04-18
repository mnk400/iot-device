'''
Created on April 6th, 2020

@author: manik
'''
from project.lib.MultiSensorAdapter import MultiSensorAdapter
from project.lib.SerialCommunicator import SerialCommunicator
from project.lib.SensorResource     import SensorResource
from project.lib.ActuatorAdapter    import ActuatorAdapter
import logging

logging.getLogger("DeviceDataManagerLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
class DeviceDataManager(object):
    '''
    Class to manage the taskAdapter and actautorAdapter and serialReader
    i.e. initialize and start them
    '''

    checksBypass = False

    def __init__(self, intervalTime=2):
        '''
        Constructor
        '''
        #setting sleep interval
        interval = intervalTime

        logging.info("Initializing Startup Sequence")
        logging.info("Starting Serial Reader Thread")
        
        #Intializing threads and Adapters
        self.serialReadThread = SerialCommunicator(115200)
        self.tasksAdapter     = MultiSensorAdapter(interval)
        self.actuatorAdapter  = ActuatorAdapter()
        self.dataStore = SensorResource.getInstance()      


    def startupSequence(self):
        '''
        Method to execute the startup sequence, 
        i.e. checking for the sensor and serial 
        and hence starting task threads
        '''

        if self.enableSerial == True:
            #Starting the serialRead
            self.serialReadThread.start()

        if self.enableAdapter == True:
            #Starting the adapter
            self.actuatorAdapter.start()

        if self.enableTasks == True:
            #Checking till sensor is available and then 
            while True:    
                if self.dataStore.status == True or self.checksBypass == True:
                    logging.info("Starting Sensor Task Threads")
                    #Executing the task threads
                    self.tasksAdapter.__execute__()
                    break
        return True


# if __name__ == "__main__":
#     manager = DeviceDataManager()
#     manager.startupSequence()
