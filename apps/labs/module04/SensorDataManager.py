'''
Created on Feb 14, 2020

@author: manik
'''

import logging
from labs.common import ConfigUtil, SensorData, ActuatorData
from labs.module04 import MultiActuatorAdapter
from labs.module02 import SmtpClientConnector
from math import floor

logging.getLogger("SensorDataManagerLogger")

class SensorDataManager(object):
    '''
    This class is responsible for Managing the SensorData instance
    This class reads a SensorData instance and then changes an ActuatorData instance
    as required, and then proceeds to Actuate using the ActuatorAdapter
    '''

    # Setting to enable or disable Email notifications, this can be changed from TempSensorAdapter too
    SEND_EMAIL_NOTIFICATION = True
    # The default subject for the Emails
    MAILTOPIC = "Notification from Temperature Adapter"

    #Setting colors to be sent 
    RED = (210,70,70)
    BLUE = (70,90,200)
    
    def __init__(self):
        '''
        Constructor
        '''
        #Creating a configUtil instance and loading the configUtil file
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfigData()

        #Reading the required nominal temperature from the config file and logging it
        self.nominal = self.config.getIntegerValue("device","nominalTemp")
        logging.info(str("Read nominal temperature from config " + str(self.nominal)))

        #Creating an actuatorData instance to store Actuator state in, and setting it's name.
        self.actuator = ActuatorData.ActuatorData()
        self.actuator.setName("Temperature Actuator Data")

        #Creating an actuatorAdapter to actuate the actual actuator.
        self.actuatorAdapter = MultiActuatorAdapter.MultiActuatorAdapter()

        #SMTP-connector to send Emails
        self.smtpConnector = SmtpClientConnector.MyClass()

    def handleSensorData(self, sensor_data: SensorData.SensorData, mailMessage: str, classType = None) -> bool:
        '''
        Function to handle and parse the data stored in an SensorData instance
        Takes a sensorData instance and the mail body string as input 
        '''
        if type(sensor_data) != SensorData.SensorData:
            return False
        #Reading current sensor value
        sensorValue = sensor_data.getCurrentValue()

        #Checking if the input value is of type HI2C, 
        #setting actuator command to increase and sending notification,
        #also setting the actuator Value.
        if classType == "HI2C":
            self.actuator.setCommand("Print")
            temp = [str(int(floor(sensorValue))), self.RED]
            self.actuator.setValue(temp)
            self.sendNotification("Current humidity details are: \n" +mailMessage) 

        #Checking if the input value is of type HUM,  
        #setting actuator command to decrease and sending notification,
        #also setting the actuator Value.
        elif classType == "HUM": 
            self.actuator.setCommand("Print")
            temp = [str(int(floor(sensorValue))), self.BLUE]
            self.actuator.setValue(temp)
            self.sendNotification("Current humidity details are: \n" +mailMessage) 

        #If any other case
        else:
            logging.error("handleSensorData: Unknown Data encountered")
            return False

        #Calling actuatorAdapter to update the actuator state.
        self.actuatorAdapter.updateActuator(self.actuator)     
        return True
        
    def sendNotification(self, messageBody) -> bool:
        '''
        Function to send a notification using SMTP client connector if the temperature is out of range
        '''
        #Check if the send email setting is on, if yes send email
        if self.SEND_EMAIL_NOTIFICATION == True:
            logging.info("Sending Notification")
            self.smtpConnector.publishMessage(self.MAILTOPIC, messageBody)  
            return True
        # If not, log the event and exit.
        else:
            logging.info("Notification not sent: Email Setting disabled")
            return True