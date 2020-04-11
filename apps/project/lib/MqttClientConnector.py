'''
Created on Mar 12, 2020

@author: manik
'''

import paho.mqtt.client as mqtt
from labs.common import DataUtil, SensorData, ActuatorData
import logging
from time import sleep

#Get a logger
logging.getLogger("mqttLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class MqttClientConnector(object):
    '''
    Class that connects to the MQTT channel and registers a
    listener which executes something when a message is received.
    '''

    #Connection States
    sensorConnected   = False
    actuatorConnected = False

    def __init__(self, sensorTopic = "topic/sensor", actuatorTopic = "topic/actuator", broker="broker.hivemq.com", port=1883):
        '''
        Constructor
        '''
        #Specifying the MQTT details
        self.brokerAddress = "broker.hivemq.com"
        self.brokerPort    = 1883

        #Specifying the topics
        self.actuatorTopic = actuatorTopic
        self.sensorTopic   = sensorTopic

        #DataUtil for JSON conversions
        self.dataUtil = DataUtil.DataUtil()
        
        try:
            #A client for the sensorData
            self.sensorClient = mqtt.Client()
            #Assigning the Callback functions
            self.sensorClient.on_connect    = self.on_sensor_connect
            self.sensorClient.on_message    = self.on_sensor_message
            self.sensorClient.on_disconnect = self.on_sensor_disconnect
            #A client for the actuatorData
            self.actuatorClient = mqtt.Client()
            #Assigning the Callback functions
            self.actuatorClient.on_connect = self.on_actuator_connect
            self.actuatorClient.on_message = self.on_actuator_message
            self.actuatorClient.on_disconnect = self.on_actuator_disconnect
        except Exception as e:
            logging.error("MQTT:Exception:Connection Issue" + str(e))    
    
    #~~~~~~~~~~~~ CALLBACK FUNCTIONS FOR SENSOR CLIENT ~~~~~~~~~~~~~~~~~~~~~~
    def on_sensor_message(self, client, userdata, message):
        '''
        On Message @callback function for sensorData
        '''
        #Decoding the received payload and logging
        msg = message.payload.decode()
        logging.info("MQTT:Recieved a new sensorData MQTT message:" + str(msg))

    def on_sensor_connect(self, client, userdata, flags, rc):
        '''
        On Connect @callback function for sensorData
        '''
        logging.info("MQTT:Connected to " + self.sensorTopic + " topic")
        #Setting the sensorConnected Value to True
        self.sensorConnected = True

    def on_sensor_disconnect(self, client, userdata, rc):
        '''
        On Disconnect @callback function for sensorData
        '''
        logging.info("MQTT:Disconnected from sensorData topic")
        #Setting the sensorConnected Value to False
        self.sensorConnected = False

    #~~~~~~~~~~~~ CALLBACK FUNCTIONS FOR ACTUATOR CLIENT ~~~~~~~~~~~~~~~~~~~~   
    def on_actuator_message(self, client, userdata, message):
        '''
        On Message @callback function for actuatorData
        '''
        #Decoding the received payload and logging
        msg = message.payload.decode()
        logging.info("MQTT:Recieved a new actuatorData MQTT message:" + str(msg))

    def on_actuator_connect(self, client, userdata, flags, rc):
        '''
        On Connect @callback function for actuatorData
        '''
        logging.info("MQTT:Connected to actuatorData topic")
        #Setting the actuatorConnected Value to True
        self.actuatorConnected = True

    def on_actuator_disconnect(self, client, userdata, rc):
        '''
        On Disconnect @callback function for actuatorData
        '''
        logging.info("MQTT:Disconnected from actuatorData topic")
        #Setting the actuatorConnected Value to False
        self.actuatorConnected = False

    #~~~~~~~~~~~~~~~~~~~ REST OF THE FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def publishActuatorData(self, actuatorData) -> bool:
        '''
        Function to publish an ActuatorData instance on the MQTT topic
        '''

        if type(actuatorData) != ActuatorData.ActuatorData:
            #Return false if wrong input
            logging.error("MQTT:Expected ActuatorData, got something else")
            return False

        if self.actuatorConnected == False:
            #Return false if connection not established
            logging.error("MQTT:Cannot publish, not connected")
            return False
        
        logging.info("MQTT:Publishing ActuatorData")
        #Converting the sensorData instance to Json
        jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData)
        #publishing the said JSON
        self.actuatorClient.publish(self.actuatorTopic,jsonStr) 
        return True

    def publishSensorData(self, sensorData: SensorData.SensorData) -> bool:
        '''
        Function to publish an SensorData instance on the MQTT topic
        '''   
        
        if type(sensorData) != SensorData.SensorData:
            #Return false if wrong input
            logging.error("MQTT:Expected SensorData, got something else")
            return False

        if self.sensorConnected == False:
            #Return false if connection not established
            logging.error("MQTT:Cannot publish, not connected")
            return False
        
        logging.info("MQTT:Publishing SensorData")
        #Converting the sensorData instance to Json
        jsonStr = self.dataUtil.toJsonFromSensorData(sensorData)
        #publishing the said JSON
        self.sensorClient.publish(self.sensorTopic,jsonStr)
        return True
    
    def connectActuatorData(self) -> bool:
        '''
        Connects to the ActuatorData MQTT topic 
        '''
        #Connecting to the actuatorClient 
        self.actuatorClient.connect(self.brokerAddress,self.brokerPort)
        self.actuatorClient.loop_start()
        return True


    def connectSensorData(self) -> bool:
        '''
        Connects the SensorData MQTT topic
        '''
        #Connecting to the sensorClient
        self.sensorClient.connect(self.brokerAddress,self.brokerPort)
        self.sensorClient.loop_start()
        return True
  

    def listenActuatorData(self) -> bool:
        '''
        Subscribes and Listens to the ActuatorData MQTT topic 
        '''
        #Return false if not connected
        if self.actuatorConnected == False:
            logging.error("MQTT:Not connected")
            return False
        #Subscribing to the actuatorClient's topic
        self.actuatorClient.subscribe(self.sensorTopic)
        return True

    def listenSensorData(self) -> bool:
        '''
        Subscribes and Listen to the SensorData MQTT topic
        '''
        #Return false if not connected
        if self.sensorConnected == False:
            logging.error("MQTT:Not connected")
            return False
        #Subscribing to the sensorClient's topic
        self.sensorClient.subscribe(self.sensorTopic)
        return True
  
    
    def disconnect(self) -> bool:
        '''
        Disconnects all MQTT topics and connections
        '''
        #Only disconnect the the clients that are connected
        #Disconnecting the sensor Client
        if self.sensorConnected == True:
            self.sensorClient.disconnect()
            self.sensorClient.loop_stop()
        #Disconnecting the actuator Client
        if self.actuatorConnected == True:    
            self.actuatorClient.disconnect()
            self.actuatorClient.loop_stop()
        return True


if __name__ == "__main__":
    mqtt = MqttClientConnector()
    s = SensorData.SensorData()
    s.addValue(10)
    mqtt.connectSensorData()
    sleep(0.0001)
    mqtt.publishSensorData(s)
    mqtt.listenSensorData()
    sleep(10)
    mqtt.disconnect()
    #mqtt.subscribeToSensorData()