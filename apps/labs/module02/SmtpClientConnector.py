'''
Created on Jan 22, 2020

@author: manik
'''
import smtplib

from labs.module02          import ConfigUtil
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText

class MyClass(object):

    def __init__(self):
        '''
        Constructer
        '''
        self.config = ConfigUtil.ConfigUtil() 
        self.config.loadConfigData()
        
    def publishMessage(self,topic,data):
        '''
        Method which connects to my G Mail SMTP server and sends out E-Mails
        '''
        host = self.config.getValue("smtp.cloud", "host")
        port = self.config.getValue("smtp.cloud", "port")
        fromAddr = self.config.getValue("smtp.cloud", "fromAddr")
        toAddr = self.config.getValue("smtp.cloud", "toAddr")
        authToken = self.config.getValue("smtp.cloud", "authToken")
            
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic 
        msgBody = str(data)
        
        msg.attach(MIMEText(msgBody)) 
        msgText = msg.as_string()
        
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken) 
        smtpServer.sendmail(fromAddr, toAddr, msgText) 
        smtpServer.close()