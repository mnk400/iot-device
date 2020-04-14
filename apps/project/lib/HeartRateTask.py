'''
Created on April 5th, 2020

@author: manik
'''
from SerialCommunicator import SerialCommunicator
from SensorResource import SensorResource
from labs.common.SensorData import SensorData
from CoAPClientConnector import CoAPClientConnector
from time import sleep
import logging
import threading
import asyncio

logging.getLogger("HeartRateTaskLogger")
class HeartRateTask(threading.Thread):
    '''
    Threaded class to read the heart-rate data 
    from the shared sensor resource.
    '''

    def __init__(self, coAPClient: CoAPClientConnector, intervalTime=2):
        '''
        Constructor
        Sets the interval time and mqttClient
        creates a sensorData instace
        '''
        self.loop = asyncio.get_event_loop()
        #Initialzing the threaded class
        threading.Thread.__init__(self, args=(self.loop,))
        self.interval = intervalTime
        self.coAPClient = coAPClient
        #Getting an instance of the shared resource
        self.dataStore = SensorResource.getInstance()
        #Initializing the sensorData instance
        self.hrSensorData = SensorData()
    
    def readData(self):
        '''
        Function to read data from the shared resource
        '''
        #Running to repeatidly read data
        while True:
            data = self.dataStore.heartRate
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("Heart Rate Monitor")
                self.coAPClient.sendSensorDataPOST(self.loop, self.hrSensorData)
            sleep(self.interval)
    
    def run(self):
        '''
        Run function for the thread to
        call readData function
        '''
        self.readData()

if __name__ == "__main__":
    coAP = CoAPClientConnector()
    sensorRead = SerialCommunicator(115200)
    sensorRead.start()
    task = HeartRateTask(coAP)
    task.run()