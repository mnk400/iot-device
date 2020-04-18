'''
Created on Apr 15, 2020

@author: manik
'''
from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
from project.lib.CoAPClientConnector import CoAPClientConnector
import logging
import asyncio
logging.getLogger("SenseHatLogger")

class SenseHatUpdater(object):
    '''
    Class to update the status on senseHat LED Matrix
    '''
    
    #Setting colours
    b = (210, 90, 90)
    e = (0, 0, 0)

    #Matrix to draw a question mark
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
        #Getting an asyncio loop
        self.loop = asyncio.get_event_loop()
        self.sense = SenseHat()
        #Clearing the senseHat
        self.clear()
        #Creating an coAP Client
        self.coAP = CoAPClientConnector(address="coap://bubblegum.lan:5683/userresponse")
        

    def updateActuator(self, actuatorData) -> bool: 
        '''
        Function which updates the state of the actuator based on the input param.
        '''
        #getting the command from actuatorData received
        command = str(actuatorData.getCommand())

        #Logging if it's an autoCheck or a manualCheck
        if actuatorData.getValue() == "manualCheck":
            logging.info("INFO: Manually Triggered User Check")
        elif actuatorData.getValue() == "autoCheck":
            logging.info("INFO: Automatically Triggered User Check")
        
        #Checking if we get the right command
        if command == "userCheck":
            logging.info("Checking up on user")
            
            #Setting the pixels on the matrix
            self.sense.set_pixels(self.QUES)

            while True:
                event = self.sense.stick.wait_for_event()
                # Check if the joystick was pressed
                if event.action == ACTION_PRESSED:
                    #Looking for response from the user
                    logging.info("RESPONSE:Sensed a button press")
                    self.clear()
                    #sending a response back saying we have recieved the response
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