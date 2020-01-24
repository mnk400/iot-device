'''
Created on Jan 22, 2020

@author: manik
'''

import configparser
import os

class ConfigUtil(object):
  

    def __init__(self):
        '''
        Constructor
        '''
        self.parser = configparser.ConfigParser()
        self.config_file = "../../../config/ConnectedDevicesConfig.props"
        self.configFileLoaded = False
        
        
    def getValue(self, section_str, key_str):
        '''
        This method returns a said key for a said section
        '''
        if self.configFileLoaded == True:
            #if section_str in self.sections:
            return self.parser[section_str][key_str]
            
    
    def hasConfigData(self):
        '''
        Method checks if any section in the config has any key
        '''
        if self.configFileLoaded != False:
            self.sections = list(self.parser.sections())
            for section in self.sections:                               #converting the list of key values
                key_set = set(self.parser[section].values())            #to a set so we can avoid a double
                if len(key_set) > 1 or list(key_set)[0] != 'Not set':   #loop when checking if any key exists
                    return True
                else:    
                    return False
        else:
            return False   
             
    def loadConfigData(self):
        '''
        Loads config data from the config file
        '''
        if os.path.exists(self.config_file):
            self.parser.read(self.config_file)
            self.configFileLoaded = True  
 
        