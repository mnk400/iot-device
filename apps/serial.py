'''
Created on April 14th, 2020

@author: manik
'''
import logging
import numpy as np

logging.getLogger("SerialEmulatorLogger")
class Serial(object):

    def __init__(self, baud, serialPort):
        logging.info("Serial Emulator")
        logging.info("Input Baud: " + str(baud))
        logging.info("Input serialPort: " + str(baud))
        self.init = True
    
    def flushInput(self):
        logging.info("Flushing Input")
    
    def readline(self):
        emuHR   = np.random.uniform(70,90,1)
        emuSPO  = np.random.uniform(85,97,1)

        emuStr  = str(emuHR[0]) + "," + str(emuSPO[0])
        
        if self.init == True:
            self.init = False
            return "Done".encode()
        else:
            return emuStr.encode()
        
    
    def write(self, strng):
        logging.info("writing to serial: " + strng)

