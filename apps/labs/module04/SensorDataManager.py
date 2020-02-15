'''
Created on Feb 6, 2020

@author: manik
'''

import logging
from labs.common import ConfigUtil, SensorData, ActuatorData
from labs.module04 import MultiActuatorAdapter
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

    #Setting values for the actuatorData
    #These values will be set on the actuator by the actuatorAdapter
    #Setting colours for the senseHAT LED matrix
    w = (90, 90, 210)
    b = (210, 90, 90)
    g = (90, 210, 90)
    e = (0, 0, 0)
    #Matrix to draw a down arrow 
    DOWN = [
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
    UP = [
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
    STABLE = [
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

    def handleSensorData(self, sensor_data: SensorData.SensorData, mailMessage: str) -> bool:
        '''
        Function to handle and parse the data stored in an SensorData instance
        Takes a sensorData instance and the mail body string as input 
        '''
        if type(sensor_data) != SensorData.SensorData:
            return False
        #Reading current sensor value
        sensorValue = sensor_data.getCurrentValue()
        
        #Checking if the temperature is greater than expected, 
        #setting actuator command to increase and sending notification,
        #also setting the actuator Value.
        if sensorValue < self.nominal - self.TOLERANCE:
            self.actuator.setCommand("Increase")
            self.actuator.setValue(self.UP)
            self.sendNotification("Temperature lower than nominal, increasing. \n" + mailMessage)  

        #Checking if the temperature is greater than expected, 
        #setting actuator command to decrease and sending notification,
        #also setting the actuator Value.
        elif sensorValue > self.nominal + self.TOLERANCE: 
            self.actuator.setCommand("Decrease")
            self.actuator.setValue(self.DOWN)
            self.sendNotification("Temperature higher than nominal, decreasing. \n" +mailMessage)  

        #Else setting the actuator to stable, if the temperature is in the same we expected to,
        #also setting the actuator Value. 
        elif sensorValue > self.nominal - self.TOLERANCE and sensorValue < self.nominal + self.TOLERANCE:
            self.actuator.setValue(self.STABLE)
            self.actuator.setCommand("Stable")

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