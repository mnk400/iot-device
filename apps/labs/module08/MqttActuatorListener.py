'''
Created on Mar 12, 2020

@author: manik
'''
from labs.module08 import MqttClientConnector
import threading
from time import sleep
import logging

logging.getLogger("AdapterLogger")

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class MqttActuatorListener(threading.Thread):
    '''
    Class to create a thread wrapped around the subscribe method in MqttClientConnector
    '''
    def __init__(self, mqttClient):
        '''
        Constructor with a reference of the mqttClient
        '''
        threading.Thread.__init__(self)
        self.mqtt = mqttClient

    def run(self):
        '''
        Run method to connect and run the listener
        '''
        self.mqtt.connectActuatorData()
        sleep(0.5)
        self.mqtt.listenActuatorData() 