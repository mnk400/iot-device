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
    Classdocs
    '''
    SEND_EMAIL_NOTIFICATION = True
    MAILTOPIC = "Notification from Temperature Adapter"
    def __init__(self):
        '''
        Constructor
        '''
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfigData()
        self.nominal = self.config.getIntegerValue("device","nominalTemp")
        logging.info(str("Read nominal temperature from config " + str(self.nominal)))
        self.actuator = ActuatorData.ActuatorData()
        self.actuator.setName("Temperature Actuator Data")
        self.actuatorAdapter = TempActuatorAdapter.TempActuatorAdapter()
        self.smtpConnector = SmtpClientConnector.MyClass()

    def handleSensorData(self, sensor_data: SensorData.SensorData) -> bool:
        sensorValue = sensor_data.getCurrentValue()
        
        if sensorValue < self.nominal:
            self.actuator.setCommand("Increase")
            
        elif sensorValue > self.nominal:
            self.actuator.setCommand("Decrease")
            self.sendNotification()  
        else:
            logging.info("Temperature Nominal")

        self.actuatorAdapter.adapterVarUpdate(self.actuator)
        self.actuatorAdapter.updateActuator()         
        return True
        
    def sendNotification(self):

        if self.SEND_EMAIL_NOTIFICATION == True:
            logging.info("Sending Notification")
            self.smtpConnector.publishMessage(self.MAILTOPIC, "notification")  
            return True
        else:
            return False