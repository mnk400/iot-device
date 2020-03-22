'''
Created on Mar 21, 2020

@author: manik
'''
import logging
import threading
from labs.module06 import MqttClientConnector
from labs.common import SensorData, PersistenceUtil
from sense_hat import SenseHat
from time import sleep

logging.getLogger("tempReaderLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class TempSensorAdapterTask(threading.Thread):
    '''
    Threaded Class which reads the temperature data from the SenseHAT.
    Stores the data in the SensorData class.
    '''
    LOOP_FOREVER = False
    enableMQTT   = False
    threadStop   = False

    def __init__(self, loop_param, sleep_param, pUtil: PersistenceUtil.PersistenceUtil,mqttClient: MqttClientConnector.MqttClientConnector):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)

        self.loop_limit     = loop_param
        self.sleep_time     = sleep_param

        #Creating a SensorData instance and setting it's name
        self.sensorData = SensorData.SensorData()
        self.sensorData.setName("Temperature Sensor Data")

        #SenseHat instance to interact with the senseHAT
        self.sense = SenseHat()

        #clearing matrix
        self.sense.clear()

        #MQTT client
        self.mqtt = mqttClient

        #PersistenceUtil
        self.pUtil = pUtil

    def run(self):
        '''
        Method to read new data from the senseHat.
        Data is then pushed to the SensorData instance
        '''
        i = 0
        
        while i < self.loop_limit or self.LOOP_FOREVER == True:
            i = i+1
            
            #break and kill thread if activated
            if self.threadStop:
                break

            #Read from senseHAT     
            humData = self.sense.get_temperature()

            #Add data to sensorData
            self.sensorData.addValue(humData)
            humString = self.generateString()

            if self.enableMQTT:
                #publish data to the MQTT topic
                self.mqtt.publishSensorData(self.sensorData)

            #Passing the Json on redis
            self.pUtil.writeSensorDataDbmsListener(self.sensorData)

            #Log the data and send the sensorData instance in the SensorDataManager
            logging.info(humString) 
            sleep(self.sleep_time)      

        return True 

    def stop(self) -> bool:
        logging.info("Quitting Thread")
        self.threadStop = True
        return True
        
    def generateString(self) -> str:
        '''
        Generate a detailed string from a sensorData instance and returns it.
        '''
        msgString  = "\nHumidity from the sense_HAT API:"
        msgString += "\n\tTime : " + self.sensorData.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensorData.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensorData.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensorData.getCount())
        return msgString

        