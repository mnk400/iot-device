'''
Created on Mar 12, 2020

@author: manik
'''

from labs.common import DataUtil, SensorData, ActuatorData, ActuatorDataListener
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
    Address = "coap://bubblegum.lan:5683/temp"
    
    def __init__(self):
        '''
        Constructor
        '''
        #DataUtil for JSON conversions
        self.dataUtil = DataUtil.DataUtil()
          
    
    #~~~~~~~~~~~~ FUNCTION FOR RECIEVING ACTUATOR DATA JSON ~~~~~~~~~~~~~~~~~~~
    def registerActuatorDataListener(self, actuatorDataListener: ActuatorDataListener.ActuatorDataListener):
        if type(actuatorDataListener) != ActuatorDataListener.ActuatorDataListener:
            return False
        return True

    #~~~~~~~~~~~~ FUNCTIONS FOR SENDING SENSOR DATA JSON  ~~~~~~~~~~~~~~~~~~~~~~
    async def dataPUT(self, jsonPayload) -> bool:
        '''
        Method to send the SensorData instance to the servor using PUT
        '''
        try:
            #Creating a context variable for CoAP
            context = await Context.create_client_context()
            #Sleep for the slightest of time
            await asyncio.sleep(0.1)
            jsonPayload = jsonPayload.encode()
            #send a rquest
            request = Message(code=PUT, payload=jsonPayload, uri=self.Address)
            #waiting for the response
            response = await context.request(request).response

            logging.info("CoAP: PUT successful " + str(response.code) + " ")
        except Exception as e:
            logging.error("CoAP: Message Delivery Failed" + str(e))
            return True
        return True

    async def dataPOST(self, jsonPayload) -> bool:
        '''
        Method to send the SensorData instance to the servor using POST
        '''
        try:
            #Creating a context variable for CoAP
            context = await Context.create_client_context()
            #Sleep for the slightest of time
            await asyncio.sleep(0.1)
            jsonPayload = jsonPayload.encode()
            #send a rquest
            request = Message(code=POST, payload=jsonPayload, uri=self.Address)
            #waiting for the response
            response = await context.request(request).response

            logging.info("CoAP: POST successful " + str(response.code) + " ")
        except Exception as e:
            logging.error("CoAP: Message Delivery Failed" + str(e))
            return True
        return True
    
    async def dataGET(self) -> bool:
        '''
        Method to get data instances from the servor using GET
        '''
        try:
            #Creating a context variable for CoAP
            context = await Context.create_client_context()
            #Sleep for the slightest of time
            await asyncio.sleep(0.1)
            #send a rquest
            request = Message(code=GET, uri=self.Address)
            #waiting for the response
            response = await context.request(request).response

            logging.info("CoAP: GET successful " + str(response.code) + " ")
        except Exception as e:
            logging.error("CoAP: GET Failed" + str(e))
            return True
        return True
    
    async def dataDelete(self) -> bool:
        '''
        Method to delete resource on the server using delete
        '''
        try:
            #Creating a context variable for CoAP
            context = await Context.create_client_context()
            #Sleep for the slightest of time
            await asyncio.sleep(0.1)
            #send a rquest
            request = Message(code=DELETE, uri=self.Address)
            #waiting for the response
            response = await context.request(request).response

            logging.info("CoAP: DELETE successful " + str(response.code) + " ")
        except Exception as e:
            logging.error("CoAP: DELETE Failed" + str(e))
            return True
        return True


    def sendSensorDataPUT(self, loop, sensorData: SensorData.SensorData) -> bool:
        '''
        Method to provide abstraction to convert sensorData to JSON and call dataSender
        '''
        if type(sensorData) != SensorData.SensorData:
            return False
        #Coverting using dataUtil
        jsonPayload = self.dataUtil.toJsonFromSensorData(sensorData)
        #Sending payload
        loop.run_until_complete(self.dataPUT(jsonPayload))
        return True

    def sendSensorDataPOST(self, loop, sensorData: SensorData.SensorData) -> bool:
        '''
        Method to provide abstraction to convert sensorData to JSON and call dataSender
        '''
        if type(sensorData) != SensorData.SensorData:
            return False
        #Coverting using dataUtil
        jsonPayload = self.dataUtil.toJsonFromSensorData(sensorData)
        #Sending payload
        loop.run_until_complete(self.dataPOST(jsonPayload))
        return True

    def getData(self, loop) -> bool:
        '''
        Method to get data from the server
        '''
        loop.run_until_complete(self.dataGET())
        return True

    def deleteData(self, loop) -> bool:
        '''
        Method to delete data from the server
        '''
        loop.run_until_complete(self.dataDelete())
        return True
        
# if __name__ == "__main__":
#     coap = CoAPClientConnector()
#     s = SensorData.SensorData()
#     s.addValue(10)
#     coap.getData(asyncio.get_event_loop())
    