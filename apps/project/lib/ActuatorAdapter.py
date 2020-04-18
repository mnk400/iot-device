'''
Created on Apr 15, 2020

@author: manik
'''
from project.lib.MqttClientConnector import MqttClientConnector
from time import sleep
import threading


class ActuatorAdapter(threading.Thread):
    '''
    Class responsible for dealing with the actuator based on what is received on MQTT
    actuatorData channel
    '''

    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.mqtt = MqttClientConnector()

    def run(self):
        '''
        Run method to execute thread
        '''
        #Connecting and subscribing to MQTT topic
        self.mqtt.connectActuatorData()
        sleep(0.5)
        self.mqtt.listenActuatorData()


# if __name__ == "__main__":
#     actuate = ActuatorAdapter()
#     actuate.run()