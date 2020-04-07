'''
Created on April 6th, 2020

@author: manik
'''
from SerialCommunicator import SerialCommunicator
from SensorResource import SensorResource
from labs.common.SensorData import SensorData
from time import sleep
import logging
import threading

logging.getLogger("SpO2TaskLogger")
class SpO2Task(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, mqttClient, intervalTime=2):
        threading.Thread.__init__(self)
        self.interval = intervalTime
        self.dataStore = SensorResource.getInstance()
        self.mqttClient = mqttClient

        self.hrSensorData = SensorData()
    
    def readData(self):
        while True:
            data = self.dataStore.spO2
            if data != None:
                self.hrSensorData.addValue(float(data))
                self.hrSensorData.setName("Blood Oxygen Monitor")
                self.mqttClient.publishSensorData(self.hrSensorData)
            sleep(self.interval)

    def run(self):
        self.readData()

if __name__ == "__main__":
    sensorRead = SerialCommunicator(115200)
    sensorRead.start()
    task = SpO2Task()
    task.run()