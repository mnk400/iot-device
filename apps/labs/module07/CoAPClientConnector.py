'''
Created on Mar 12, 2020

@author: manik
'''

from labs.common import DataUtil, SensorData, ActuatorData
from time import sleep
from aiocoap import *
import asyncio
import logging

#Get a logger
logging.getLogger("CoAPLogger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class CoAPClientConnector(object):
    '''
    Class that connects to CoAP and registers a
    listener which executes something when a message is received.
    '''

    #Specifying the coAP details
    Address = "coap://squishypi.lan/other/block"

    #Connection States
    sensorConnected   = False
    actuatorConnected = False

    def __init__(self):
        '''
        Constructor
        '''
        #DataUtil for JSON conversions
        self.dataUtil = DataUtil.DataUtil()
          
    
    #~~~~~~~~~~~~ FUNCTION FOR RECIEVING ACTUATOR DATA JSON ~~~~~~~~~~~~~~~~~~~
    def registerActuatorDataListener(self, ActuatorDataListener):
        return True

    #~~~~~~~~~~~~ FUNCTIONS FOR SENDING SENSOR DATA JSON  ~~~~~~~~~~~~~~~~~~~~~~
    async def dataSender(self, jsonPayload) -> bool:
        '''
        Method to send the SensorData instance to the servor using PUT
        '''
        try:
            #Creating a context variable for CoAP
            context = await Context.create_client_context()
            #Sleep for the slightest of timez
            await asyncio.sleep(0.1)
            jsonPayload = jsonPayload.encode()
            #send a rquest
            request = Message(code=PUT, payload=jsonPayload, uri=self.Address)
            #waiting for the response
            response = await context.request(request).response

            logging.info("CoAP: PUT successful " + str(response.code) + " ")
        except Exception as e:
            logging.error("CoAP: Message Delivery Failed")
            print(e)
            return False

        return True


    def sendSensorData(self, loop, sensorData: SensorData.SensorData) -> bool:
        '''
        Method to convert sensorData to JSON and call dataSender
        '''
        #Coverting using dataUtil
        jsonPayload = self.dataUtil.toJsonFromSensorData(sensorData)
        #Sending payload
        loop.run_until_complete(self.dataSender(jsonPayload))
            


if __name__ == "__main__":
    coap = CoAPClientConnector()
    s = SensorData.SensorData()
    s.addValue(10)
    coap.sendSensorData(s)
    