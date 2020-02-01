'''
Created on Jan 22, 2020

@author: manik
'''
import logging
import smtplib

from labs.common          import ConfigUtil
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText

logging.getLogger("smtpLog")                      #Get a logger instance
class MyClass(object):
    '''
    This class is responsible for connecting to a SMTP server and sending out Emails
    Uses email.mime from MIMETest and MIMEMultipart to form MIME emails
    '''
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
        port = self.config.getIntegerValue("smtp.cloud", "port")
        fromAddr = self.config.getValue("smtp.cloud", "fromAddr")
        toAddr = self.config.getValue("smtp.cloud", "toAddr")
        authToken = self.config.getValue("smtp.cloud", "authToken")
        #creating the message in MIME format
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic 
        msgBody = str(data)
        #attaching the message Body to the message
        msg.attach(MIMEText(msgBody)) 
        msgText = msg.as_string()      
        #The piece of code below will connect to the SMTP server
        #and send out the email containing the message
        #does follow RFC 821 as of 27th Jan '20
        try:
            #specify host and port for the SMTP
            smtpServer = smtplib.SMTP_SSL(host, port) 
            smtpServer.ehlo()                             
            #specify from and authToken           
            smtpServer.login(fromAddr, authToken)
            #specify from, to and msgText in MIME format                   
            smtpServer.sendmail(fromAddr, toAddr, msgText)        
            #close server
            smtpServer.close()
        except Exception as e:
            #returning false in issues of an error and logging the event
            logging.error("SMTP cannot connect" + str(e))
            return False
        #returning true if program works as intended and logging    
        logging.info("Email sent")    
        return True        