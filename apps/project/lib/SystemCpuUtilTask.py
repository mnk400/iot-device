'''
Created on Jan 15, 2020

@author: manik
'''
import psutil
import threading
import asyncio
from time import sleep
from labs.common.SensorData import SensorData
from CoAPClientConnector import CoAPClientConnector 

class Cpu(threading.Thread):

    def __init__(self, coAPClient: CoAPClientConnector, intervalTime=15):
        '''
        Constructor
        '''
        self.loop = asyncio.get_event_loop()
        #Initialzing the threaded class
        threading.Thread.__init__(self, args=(self.loop,))
        self.interval = intervalTime
        self.coAPClient = coAPClient
        #Initializing the sensorData instance
        self.hrSensorData = SensorData()

    def getCpu(self):
        '''
        Method to return percentage of CPU being used
        '''
        psutil.cpu_percent(interval=1)
        #Running to repeatidly read data
        while True:
            data = psutil.cpu_percent(interval=1)
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("CPU Usage")
                self.coAPClient.sendSensorDataPOST(self.loop, self.hrSensorData)
            sleep(self.interval)
    
    def run(self):
        self.getCpu()

if __name__ == "__main__":
    coAP = CoAPClientConnector("coap://bubblegum.lan:5683/cpu")
    task = Cpu(coAP)
    task.start()