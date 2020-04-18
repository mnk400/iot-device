'''
Created on April 6th, 2020

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

logging.getLogger("SpO2TaskLogger")
class SpO2Task(threading.Thread):
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
        self.asyncLoop = asyncio.get_event_loop()
        self.looplimit = looplimit
        #Initialzing the threaded class
        threading.Thread.__init__(self, args=(self.asyncLoop,))
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
        i=0
        #Initialzing the threaded class
        while True:
            i = i+1
            data = self.dataStore.spO2
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:    
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("Blood Oxygen Monitor")
                self.coAPClient.sendSensorDataPOST(self.asyncLoop, self.hrSensorData)
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
#     coAP = CoAPClientConnector("coap://bubblegum.lan:5683/spo")
#     sensorRead = SerialCommunicator(115200)
#     sensorRead.start()
#     task = SpO2Task(coAP)
#     task.run()