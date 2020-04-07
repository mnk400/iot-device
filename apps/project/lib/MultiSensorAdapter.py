'''
Created on April 6th, 2020

@author: manik
'''
from HeartRateTask import HeartRateTask
from SpO2Task import SpO2Task
from SerialCommunicator import SerialCommunicator
from MqttClientConnector import MqttClientConnector
import logging

logging.getLogger("SensorAdaptetLogger")
class MultiSensorAdapter(object):
    '''
    classdocs
    '''

    def __init__(self, intervalTime=2):

        self.mqttHR = MqttClientConnector("topic/hrsensor")
        self.mqttHR.connectSensorData()

        self.mqttSP = MqttClientConnector("topic/spo2sensor")
        self.mqttSP.connectSensorData()

        self.taskHR     = HeartRateTask(self.mqttHR, intervalTime)   
        self.taskSpO2   = SpO2Task(self.mqttSP, intervalTime)     

    def __execute__(self):
        self.taskHR.start()
        self.taskSpO2.start()

if __name__ == "__main__":
    sensorRead = SerialCommunicator(115200)
    sensorRead.start()
    task = MultiSensorAdapter()
    task.__execute__()