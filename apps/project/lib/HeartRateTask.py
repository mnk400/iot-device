'''
Created on April 5th, 2020

@author: manik
'''
from project.lib.SerialCommunicator import SerialCommunicator
from project.lib.SensorResource import SensorResource
from labs.common.SensorData import SensorData
from project.lib.CoAPClientConnector import CoAPClientConnector
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

    def __init__(self, coAPClient: CoAPClientConnector, intervalTime=2, looplimit=-1):
        '''
        Constructor
        Sets the interval time and mqttClient
        creates a sensorData instace
        '''
        self.loop = asyncio.get_event_loop()
        self.looplimit = looplimit
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
        i = 0
        #Running to repeatidly read data
        while True:
            i = i + 1
            data = self.dataStore.heartRate
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("Heart Rate Monitor")
                self.coAPClient.sendSensorDataPOST(self.loop, self.hrSensorData)
            sleep(self.interval)
            
            if self.looplimit != -1:
                if i == self.looplimit:
                    break
    
    def run(self):
        '''
        Run function for the thread to
        call readData function
        '''
        self.readData()
        return True

# if __name__ == "__main__":
#     coAP = CoAPClientConnector("coap://bubblegum.lan:5683/heartrate")
#     sensorRead = SerialCommunicator(115200)
#     sensorRead.start()
#     task = HeartRateTask(coAP)
#     task.run()