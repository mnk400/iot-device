'''
Created on April 6th, 2020

@author: manik
'''
from HeartRateTask import HeartRateTask
from SpO2Task import SpO2Task
from SerialCommunicator import SerialCommunicator
from CoAPClientConnector import CoAPClientConnector
from MqttClientConnector import MqttClientConnector
from SystemCpuUtilTask import Cpu
from SystemMemUtilTask import Mem
import logging
import asyncio

logging.getLogger("SensorAdaptetLogger")
class MultiSensorAdapter(object):
    '''
    classdocs
    '''
    #Specifying the coAP details
    addressHR  = "coap://bubblegum.lan:5683/heartrate"
    addressSP  = "coap://bubblegum.lan:5683/spo"
    addressCpu = "coap://bubblegum.lan:5683/cpu"
    addressMem = "coap://bubblegum.lan:5683/mem"

    def __init__(self, intervalTime=5):
        #self.mqttHR = MqttClientConnector("topic/hrsensor")

        self.coapHR  = CoAPClientConnector(self.addressHR)
        self.coapSP  = CoAPClientConnector(self.addressSP)
        self.coapCpu = CoAPClientConnector(self.addressCpu)
        self.coapMem = CoAPClientConnector(self.addressMem)

        self.taskHR     = HeartRateTask(self.coapHR, intervalTime)   
        self.taskSpO2   = SpO2Task(self.coapSP, intervalTime) 
        self.taskCpu    = Cpu(self.coapCpu)
        self.taskMem    = Cpu(self.coapMem)   

    def __execute__(self):
        self.taskHR.start()
        self.taskSpO2.start()
        self.taskCpu.start()
        self.taskMem.start()

if __name__ == "__main__":
    sensorRead = SerialCommunicator(115200)
    sensorRead.start()
    task = MultiSensorAdapter()
    task.__execute__()