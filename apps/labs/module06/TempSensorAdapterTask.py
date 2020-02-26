'''
Created on Feb 26, 2020

@author: manik
'''
import logging
import threading
from labs.common import SensorData, PersistenceUtil
from sense_hat import SenseHat
from time import sleep

logging.getLogger("tempReaderLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class TempSensorAdapterTask(threading.Thread):
    '''
    Threaded Class which reads the temperature data from the SenseHAT.
    Stores the data in the SensorData class.
    '''
    LOOP_FOREVER = False
    def __init__(self, loop_param, sleep_param, pUtil: PersistenceUtil.PersistenceUtil):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)

        self.loop_limit     = loop_param
        self.sleep_time     = sleep_param

        #Creating a SensorData instance and setting it's name
        self.sensorData = SensorData.SensorData()
        self.sensorData.setName("Temperature Sensor Data")

        #SenseHat instance to interact with the senseHAT
        self.sense = SenseHat()

        #clearing matrix
        self.sense.clear()

        #PersistenceUtil reference
        self.pUtil = pUtil
        pass

    def run(self):
        '''
        Method to read new data from the senseHat.
        Data is then pushed to the SensorData instance
        '''
        i = 0
        try:
            while i < self.loop_limit or self.LOOP_FOREVER == True:
                i = i+1
                #Read from senseHAT     
                humData = self.sense.get_temperature()

                #Add data to sensorData
                self.sensorData.addValue(humData)

                # ~~ Replace with MQTT code

                # #Passing the Json on redis
                # self.pUtil.writeSensorDataDbmsListener(self.sensorData)
                # #Generate a will detailed string
                humString = self.generateString()

                #Log the data and send the sensorData instance in the SensorDataManager
                logging.info(humString) 
                sleep(self.sleep_time)
        except (KeyboardInterrupt):
            logging.info("Received keyboard interrupt, quitting threads.\n")
            self.sense.clear()
            return True        
        return True 

    def generateString(self) -> str:
        '''
        Generate a detailed string from a sensorData instance and returns it.
        '''
        msgString  = "\nHumidity from the sense_HAT API:"
        msgString += "\n\tTime : " + self.sensorData.timestamp
        msgString += "\n\tCurrent : " + repr(self.sensorData.getCurrentValue())
        msgString += "\n\tAverage : " + repr(self.sensorData.getAverageValue())
        msgString += "\n\tSamples : " + repr(self.sensorData.getCount())
        return msgString

        