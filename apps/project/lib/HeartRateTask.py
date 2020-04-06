'''
Created on April 5th, 2020

@author: manik
'''
from SerialCommunicator import SerialCommunicator
from sensorResource import sensorResource
from time import sleep
class HeartRateTask(object):
    '''
    classdocs
    '''

    def __init__(self):
        
        sensorRead = SerialCommunicator(115200)
        sensorRead.start()
        self.dataStore = sensorResource.getInstance()
    
    def readData(self):
        while True:
            if(self.dataStore.status == False):
                sleep(2)
                print("Heart Rate: " + str(self.dataStore.heartRate))
                print("SPO2: " + str(self.dataStore.spO2))

if __name__ == "__main__":
    task = HeartRateTask()
    task.readData()