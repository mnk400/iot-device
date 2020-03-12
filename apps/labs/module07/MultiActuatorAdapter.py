'''
Created on Mar 12, 2020

@author: manik
'''
import logging
from sense_hat import SenseHat
from labs.common import ActuatorData 
from time import sleep

logging.getLogger("ActuatorAdapterLogger")

class MultiActuatorAdapter(object):
    '''
    This class is responsible for changing the state of the actuator, 
    based on the information in the instance of actuatorData passed in the class.
    '''
    #Setting values for the actuatorData
    #These values will be set on the actuator by the actuatorAdapter
    #Setting colours for the senseHAT LED matrix
    w = (90, 90, 210)
    b = (210, 90, 90)
    g = (90, 210, 90)
    e = (0, 0, 0)
    #Matrix to draw a down arrow 
    DOWNARROW = [
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                w,w,w,w,w,w,w,w,
                e,w,w,w,w,w,w,e,
                e,e,e,w,w,e,e,e
            ]
    #Matrix to draw an up arrow
    UPARROW = [
                e,e,e,b,b,e,e,e,
                e,b,b,b,b,b,b,e,
                b,b,b,b,b,b,b,b,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e
            ]    
    #Matrix to draw a tick mark
    TICK = [
                e,e,e,e,e,e,e,e,
                e,e,e,e,e,e,e,g,
                e,e,e,e,e,e,g,g,
                e,e,e,e,e,g,g,e,
                g,e,e,e,g,g,e,e,
                g,g,e,g,g,e,e,e,
                e,g,g,g,e,e,e,e,
                e,e,g,e,e,e,e,e
            ] 
    def __init__(self):
        '''
        Constructor
        '''
        self.sense = SenseHat()

    def updateActuator(self, actuator_param) -> bool: 
        '''
        Function which updates the state of the actuator based on the input param.
        '''
        self.actuator = actuator_param
        
        #Reading the command from the actuatorData instance
        strCheck = str(self.actuator.getCommand())
        
        #Reading actuator value from actuatorData instance
        acValue = self.actuator.getValue()
        if acValue == "UPARROW": acValue = self.UPARROW 
        elif acValue == "DOWNARROW": acValue = self.DOWNARROW
        elif acValue == "TICK": acValue = self.TICK
        
        if strCheck == "Print":
            self.clear()
            #Checking the length of the input to determine the best display method to use
            if len(acValue[0]) <2:
                #If one, simply printing the letter
                self.sense.show_letter(acValue[0],acValue[1])
                return True
            elif len(acValue[0]) >=2:
                #If more than one, printing a rolling message
                self.sense.show_message(acValue[0], text_colour=acValue[1], scroll_speed=0.07)
                return True   
            else:
                logging.info("Actuator Value can not be empty when trying to print")
                return False  

        #If increase, logging and setting the LED to display a up and return true.
        elif strCheck == "Increase":
            #logging.info("Actuator: Increasing Temp")
            self.clear()
            self.sense.set_pixels(acValue)
            return True
        
        #If decrease, logging and setting the LED to display a down and return true.  
        elif strCheck == "Decrease":
            #logging.info("Actuator: Decreasing Temp")  
            self.clear()
            self.sense.set_pixels(acValue)
            return True
        
        #If stable then setting a tick mark on the matrix and returning true.    
        elif strCheck == "Stable":
            #logging.info("Temperature Stable")
            self.clear()
            self.sense.set_pixels(acValue)
            return True    
        
        #If none of those, then returning a false and logging error    
        else:
            logging.error("Unknown Actuator Command")
            return False
            
        return False
        
    def clear(self) -> bool:
        '''
        Simple method to clear the LED matrix
        '''
        self.sense.clear()
        return True
  