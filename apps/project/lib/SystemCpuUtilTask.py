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

class Cpu(threading.Thread):
    '''
    Class to create a threaded task to report the system CPU and 
    memory usage using coAP
    '''

    def __init__(self, coAPClient: CoAPClientConnector, intervalTime=20, looplimit=-1):
        '''
        Constructor
        '''
        #Get an asyncio loop
        self.loop = asyncio.get_event_loop()
        self.looplimit = looplimit
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
        i=0
        psutil.cpu_percent(interval=1)
        #Running to repeatidly read data
        while True:
            i = i+1
            data = psutil.cpu_percent(interval=1)
            #Only adding the data to sensorData instance
            #if it's not None
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("CPU Usage")
                self.coAPClient.sendSensorDataPOST(self.loop, self.hrSensorData)
            sleep(self.interval)

            if self.looplimit != -1:
                if i == self.looplimit:
                    break
    
    def run(self):
        self.getCpu()
        return True

# if __name__ == "__main__":
#     coAP = CoAPClientConnector("coap://bubblegum.lan:5683/cpu")
#     task = Cpu(coAP)
#     task.start()