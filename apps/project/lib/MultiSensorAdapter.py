'''
Created on April 6th, 2020

@author: manik
'''
from project.lib.HeartRateTask import HeartRateTask
from project.lib.SpO2Task import SpO2Task
from project.lib.SerialCommunicator import SerialCommunicator
from project.lib.CoAPClientConnector import CoAPClientConnector
from project.lib.MqttClientConnector import MqttClientConnector
from project.lib.SystemCpuUtilTask import Cpu
from project.lib.SystemMemUtilTask import Mem
import logging
import asyncio

logging.getLogger("SensorAdaptetLogger")
class MultiSensorAdapter(object):
    '''
    Class to initialize and execute all the tasks
    '''
    #Specifying the coAP details
    addressHR  = "coap://bubblegum.lan:5683/heartrate"
    addressSP  = "coap://bubblegum.lan:5683/spo"
    addressCpu = "coap://bubblegum.lan:5683/cpu"
    addressMem = "coap://bubblegum.lan:5683/mem"

    def __init__(self, intervalTime=10):
        '''
        Constructor
        '''

        #Creating four coAP Clients for each task thread
        self.coapHR  = CoAPClientConnector(self.addressHR)
        self.coapSP  = CoAPClientConnector(self.addressSP)
        self.coapCpu = CoAPClientConnector(self.addressCpu)
        self.coapMem = CoAPClientConnector(self.addressMem)

        #Intializing each thread
        self.taskHR     = HeartRateTask(self.coapHR, intervalTime)   
        self.taskSpO2   = SpO2Task(self.coapSP, intervalTime) 
        self.taskCpu    = Cpu(self.coapCpu)
        self.taskMem    = Cpu(self.coapMem)   

    def __execute__(self):
        '''
        Method to execute all threads
        '''
        #Starting all threads one by one
        self.taskHR.start()
        self.taskSpO2.start()
        self.taskCpu.start()
        self.taskMem.start()

# if __name__ == "__main__":
#     sensorRead = SerialCommunicator(115200)
#     sensorRead.start()
#     task = MultiSensorAdapter()
#     task.__execute__()