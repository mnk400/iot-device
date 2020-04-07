'''
Created on April 6th, 2020

@author: manik
'''
from MultiSensorAdapter import MultiSensorAdapter
from SerialCommunicator import SerialCommunicator
from SensorResource     import SensorResource
import logging

logging.getLogger("DeviceDataManagerLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
class DeviceDataManager(object):
    '''
    classdocs
    '''
    def __init__(self, intervalTime=2):
        interval = intervalTime

        logging.info("Initializing Startup Sequence")
        logging.info("Starting Serial Reader Thread")
        
        self.serialReadThread = SerialCommunicator(115200)
        self.tasksAdapter     = MultiSensorAdapter(interval)
        self.dataStore = SensorResource.getInstance()       

    def startupSequence(self):
        '''
        docs
        '''
        self.serialReadThread.start()

        while True:    
            if self.dataStore.status == True:
                logging.info("Starting Sensor Task Threads")
                self.tasksAdapter.__execute__()
                break
            
        

        

if __name__ == "__main__":
    manager = DeviceDataManager()
    manager.startupSequence()
