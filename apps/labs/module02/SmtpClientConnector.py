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
        Constructor
        '''
        self.config = ConfigUtil.ConfigUtil()                   #creating a configUtil object to retrieve config data from
        self.config.loadConfigData()                            #load the config data
        
    def publishMessage(self,topic,data):
        '''
        Method which connects to my G Mail SMTP server using email.mime and sends out E-Mails
        MIME stand for Multipurpose Internet Mail Extensions
        Email subject and data are method inputs
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
        
        #The piece of code below will connect to the SMTP server
        #and send out the email containing the message
        #does follow RFC 821 as of 27th Jan '20
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()                                        
        smtpServer.login(fromAddr, authToken)                   
        smtpServer.sendmail(fromAddr, toAddr, msgText)         
        smtpServer.close()