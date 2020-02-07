'''
Created on Feb 6, 2020

@author: manik
'''

import logging
from labs.common import ConfigUtil, SensorData, ActuatorData
from labs.module03 import TempActuatorAdapter
from labs.module02 import SmtpClientConnector

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
    # Tolerance of temperature, after which the actuator will be actuated. 
    # e.g. for a read nominal temperature of 20 degrees, actuator will be enabled if it gets out of the range [17,23]
    TOLERANCE = 3

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
        self.actuatorAdapter = TempActuatorAdapter.TempActuatorAdapter()
        #SMTP-connector to send Emails
        self.smtpConnector = SmtpClientConnector.MyClass()

    def handleSensorData(self, sensor_data: SensorData.SensorData, mailMessage: str) -> bool:
        '''
        Function to handle and parse the data stored in an SensorData instance
        Takes a sensorData instance and the mail body string as input 
        '''
        #Reading current sensor value
        sensorValue = sensor_data.getCurrentValue()
        #Checking if the temperature is greater than expected, setting actuator command to increase and sending notification.
        if sensorValue < self.nominal - self.TOLERANCE:
            self.actuator.setCommand("Increase")
            self.sendNotification("Temperature lower than nominal, increasing. \n" + mailMessage)  
        #Checking if the temperature is greater than expected, setting actuator command to decrease and sending notification.
        elif sensorValue > self.nominal + self.TOLERANCE: 
            self.actuator.setCommand("Decrease")
            self.sendNotification("Temperature higher than nominal, decreasing. \n" +mailMessage)  
        #Else setting the actuator to stable, if the temperature is in the same we expected to. 
        else:
            self.actuator.setCommand("Stable")
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