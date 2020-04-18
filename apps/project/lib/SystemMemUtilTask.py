'''
Created on Jan 15, 2020

@author: manik
'''
import psutil
import threading
import asyncio
from time import sleep
from labs.common.SensorData import SensorData
from project.lib.CoAPClientConnector import CoAPClientConnector


class Mem(threading.Thread):
    '''
    Class to create a threaded task to report the system CPU and 
    memory usage using coAP
    '''

    def __init__(self, coAPClient: CoAPClientConnector, intervalTime=20, looplimit=-1):
        '''
        Constructor
        '''
        #Get an event loop
        self.loop = asyncio.get_event_loop()
        self.looplimit = looplimit
        #Initialzing the threaded class
        threading.Thread.__init__(self, args=(self.loop,))
        self.interval = intervalTime
        self.coAPClient = coAPClient
        
        #Initializing the sensorData instance
        self.hrSensorData = SensorData()


    def getRam(self):
        '''
        Method to return percentage of system memory being used
        '''
        i=0
        while True:
            i = i+1
            data = psutil.virtual_memory()[2]
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("Memory Usage")
                self.coAPClient.sendSensorDataPOST(self.loop, self.hrSensorData)
            sleep(self.interval)

            if self.looplimit != -1:
                if i == self.looplimit:
                    break
    
    def run(self):
        self.getRam()
        return True

if __name__ == "__main__":
    coAP = CoAPClientConnector("coap://bubblegum.lan:5683/mem")
    task = Mem(coAP)
    task.start()