'''
Created on Feb 6, 2020

@author: manik
'''

import logging
from sense_hat import SenseHat
from labs.common import ActuatorData 
from time import sleep
logging.getLogger("ActuatorAdapterLogger")
class TempActuatorAdapter(object):
    '''
    Classdocs
    '''
    w = (150, 150, 150)
    b = (0, 0, 255)
    e = (0, 0, 0)

    image = [
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                e,e,b,w,w,e,e,e,
                e,e,e,w,w,e,e,e,
                w,w,w,w,w,w,w,w,
                e,w,w,w,w,w,w,e,
                e,e,e,w,w,e,e,e
            ]
            
    def __init__(self):
        self.sense = SenseHat()
    
    def adapterVarUpdate(self, actuator_param: ActuatorData.ActuatorData):
        self.actuator = actuator_param

    def updateActuator(self ) -> bool: 
        if self.actuator.getCommand() == "Increase":
            logging.info("Increasing Temp")
            self.sense.show_letter("I")
        elif self.actuator.getCommand() == "Decrease":
            logging.info("Decreasing Temp")  
            #self.sense.show_letter("D") 
            self.sense.set_pixels(self.image)
        elif self.actuator.getCommand() == "Stable":
            pass
        else:
            logging.info("Unknown Command")
            return False    

        sleep(3)
        self.sense.clear()
        return True    

