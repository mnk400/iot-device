'''
Created on Jan 22, 2020

@author: manik
'''

import configparser
import os
import logging
logging.getLogger("ConfigLog")
class ConfigUtil(object):
  
    defaultConfigPath = "config/ConnectedDevicesConfig.props"
    
    def __init__(self, path_param = defaultConfigPath):
        '''
        Constructor
        '''
        self.parser = configparser.ConfigParser()
        self.filepath = path_param        #Path to the configuration file from current Dir
        self.configFileLoaded = False                                                
        
    def getValue(self, section_str, key_str):
        '''
        This method returns a said key for the asked section
        '''
        if self.configFileLoaded == True:
            #if section_str in self.sections:
            try:
                return self.parser[section_str][key_str]
            except Exception as e:
                logging.error(e)
                return False
        else:
            logging.error("Config File not loaded")
            return False    
  
    def getIntegerValue(self, section_str, key_str):
        '''
        This method returns a said key for the asked section
        '''
        if self.configFileLoaded == True:
            try:
                return int(self.parser[section_str][key_str])
            except Exception as e:
                logging.error(e)
                return False   
        else:
            logging.error("Config Filt not loaded")    
            return False     


    def getBooleanValue(self, section_str, key_str):
        '''
        This method returns a said key for the asked section
        '''
        if self.configFileLoaded == True:
            try:
                return self.parser.getboolean(section_str,key_str)
            except Exception as e:
                logging.error(e) 
                return None
        else:
            logging.error("Config File not loaded")
            return None                 
            
    def hasConfigData(self):
        '''
        Method checks if any section in the config has any key.
        Returns a true if yes, else returns a false.
        '''
        if self.configFileLoaded != False:
            self.sections = list(self.parser.sections())
            for section in self.sections:                                   #converting the list of key values
                key_set = set(self.parser[section].values())                #to a set so we can avoid a double
                if len(key_set) > 1 or list(key_set)[0] != 'Not set':       #loop when checking if any key exists
                    return True
                else:    
                    return False
        else:
            return False   
             
    def loadConfigData(self):
        '''
        Method to load config data from the config file
        '''                                                   
        if os.path.exists(self.filepath):                           
            self.parser.read(self.filepath)                         
            self.configFileLoaded = True  
            return True
        else:    
            logging.error("can not find file")
            return False  
