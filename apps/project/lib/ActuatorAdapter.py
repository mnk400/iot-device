'''
Created on Apr 15, 2020

@author: manik
'''
from MqttClientConnector import MqttClientConnector
from time import sleep
import threading


class ActuatorAdapter(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.mqtt = MqttClientConnector()

    def run(self):
        self.mqtt.connectActuatorData()
        sleep(0.5)
        self.mqtt.listenActuatorData()


if __name__ == "__main__":
    actuate = ActuatorAdapter()
    actuate.run()