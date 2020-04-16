'''
Created on Apr 15, 2020

@author: manik
'''
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
#from MqttClientConnector import MqttClientConnector
from time import sleep
from CoAPClientConnector import CoAPClientConnector
import logging
import asyncio
logging.getLogger("SenseHatLogger")

class SenseHatUpdater(object):
    b = (210, 90, 90)
    e = (0, 0, 0)
    #Matrix to draw an up arrow
    QUES = [
                e,e,e,b,b,e,e,e,
                e,b,b,e,b,b,e,e,
                b,b,b,e,e,b,b,e,
                e,e,e,e,e,b,b,e,
                e,e,e,e,b,b,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,e,e,e,e,e,
                e,e,b,b,e,e,e,e
            ]  

    def __init__(self):
        '''
        Constructor
        '''
        self.loop = asyncio.get_event_loop()
        self.sense = SenseHat()
        self.clear()
        self.coAP = CoAPClientConnector(address="coap://bubblegum.lan:5683/userresponse")
        

    def updateActuator(self, actuatorData) -> bool: 
        '''
        Function which updates the state of the actuator based on the input param.
        '''
        command = str(actuatorData.getCommand())

        if actuatorData.getValue() == "manualCheck":
            logging.info("INFO: Manually Triggered User Check")
        elif actuatorData.getValue() == "autoCheck":
            logging.info("INFO: Automatically Triggered User Check")
        
        if command == "userCheck":
            logging.info("Checking up on user")
            
            self.sense.set_pixels(self.QUES)

            while True:
                event = self.sense.stick.wait_for_event()
                # Check if the joystick was pressed
                if event.action == ACTION_PRESSED:
                    logging.info("RESPONSE:Sensed a button press")
                    self.clear()
                    self.coAP.sendAnyDataPUT(self.loop, "User Ok")
                    return True
            
        else:
            logging.info("Unknown Command")
            return False
        print("Exiting")
        return False
            
    
    def clear(self) -> bool:
        '''
        Simple method to clear the LED matrix
        '''
        self.sense.clear()
        return True