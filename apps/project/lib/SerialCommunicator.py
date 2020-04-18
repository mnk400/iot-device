'''
Created on April 5, 2020

@author: manik
'''
import serial
from time import sleep
import logging
import threading
from project.lib.SensorResource import SensorResource


logging.getLogger("SerialLogger")
class SerialCommunicator(threading.Thread):
    '''
    Class to communicate with the serial port on 
    raspberry pi with arduino which acts like
    the A/D converter for us.
    '''

    def __init__(self, baud, serialPort="/dev/ttyACM0", looplimit=-1):
        '''
        Constructor
        For setting the baudrate and the serial port.
        This constructor opens up a serial connection.
        '''
        self.looplimit = looplimit
        threading.Thread.__init__(self)
        self.baudRate = baud
        self.serialPort = serialPort
        self.dataStore = SensorResource.getInstance()

        #Initialize the serial port
        try:
            self.ser = serial.Serial(serialPort, baud)
            self.serialConencted = True
            #Flushing rogue inputs
            self.ser.flushInput()
            logging.info("SERIAL:Sensor Initializing")
        except Exception as e:
            logging.error("SERIAL:Could not connect to serial, is the sensor powered on? " + str(e))
            self.serialConencted = False
    
    def serialRead(self) -> str:
        '''
        Function to read from the serialPort
        '''
        i=0
        while True:
            i=i+1
            #Checking if serial is connected
            if(self.serialConencted == True):
                try:
                    #Reading from serial
                    b = self.ser.readline()
                    #decoding and striping of all '/n' and '/t'
                    stringRead = b.decode()
                    stringRead = stringRead.rstrip()

                    #If sensor is up and running
                    if self.dataStore.status == True:
                        #Then split the data read
                        stringRead = stringRead.split(',')
                        #And store into our shared resource
                        self.dataStore.heartRate = stringRead[0]
                        self.dataStore.spO2 = stringRead[1]
                    
                    if stringRead == "Done" and self.dataStore.status == False:
                        #First thing we look for is a 'Done' message from the serialRead
                        #Signifying our sensor is ready
                        self.dataStore.status = True
                        logging.info("SERIAL:Sensor ready")

                except Exception as e:
                    logging.error("SERIAL:Exception while reading" + str(e))         

            else: 
                self.dataStore.heartRate = 0
                self.dataStore.spO2 = 0

            if self.looplimit != -1:
                if i == self.looplimit:
                    break

        return True
    
    def serialWrite(self, wrtString) -> bool:
        '''
        Function to write to the serialPort
        '''

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
        
    
# if __name__ == "__main__":
#     temp = SerialCommunicator(115200)
#     temp.start()