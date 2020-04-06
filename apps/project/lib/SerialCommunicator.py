'''
Created on April 5, 2020

@author: manik
'''
import serial
from time import sleep
import logging
import threading
from sensorResource import sensorResource

logging.getLogger("SerialLogger")

class SerialCommunicator(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, baud, serialPort="/dev/ttyACM0"):
        '''
        Constructor
        For setting the baudrate and the serial port.
        This constructor opens up a serial connection.
        '''
        threading.Thread.__init__(self)
        self.baudRate = baud
        self.serialPort = serialPort
        self.dataStore = sensorResource.getInstance()

        #Initialize the serial port
        try:
            self.ser = serial.Serial(serialPort, baud)
            self.serialConencted = True
            self.ser.flushInput()
        except Exception as e:
            logging.error("SERIAL:Could not connect to serial" + str(e))
            self.serialConencted = False
    
    def serialRead(self) -> str:
        '''
        Function to read from the serialPort
        '''
        while True:
            if(self.serialConencted == True):
                try:
                    b = self.ser.readline()
                    stringRead = b.decode()
                    stringRead = stringRead.rstrip()
                    
                    if self.dataStore.status == True:
                        stringRead = stringRead.split(',')
                        self.dataStore.heartRate = stringRead[0]
                        self.dataStore.spO2 = stringRead[1]
                    
                    if stringRead == "Done" and self.dataStore.status == False:
                        self.dataStore.status = True

                except Exception as e:
                    logging.error("SERIAL:Exception while reading" + str(e))         

            else: 
                self.dataStore.heartRate = 0
                self.dataStore.spO2 = 0

        return stringRead
    
    def serialWrite(self, wrtString) -> bool:
        '''
        Function to write to the serialPort
        '''
        
        if self.serialConencted == False:
            return False

        try:
            self.ser.write(wrtString)
        except Exception as e:
            logging.error("SERIAL:Exception while writing")
            logging.error(e)
            return False
        
        return True
    
    def close(self):
        '''
        Function to close the serial connection
        '''
        if self.serialConencted == True:
            self.ser.close()
    
    def run(self):
        self.serialRead()
        
    
if __name__ == "__main__":
    temp = SerialCommunicator(115200)
    temp.start()