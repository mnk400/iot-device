'''
Created on Jan 22, 2020

@author: manik
'''

import configparser
import os

class ConfigUtil(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.config_file = "../../../config/ConnectedDevicesConfig.props"
        self.configFileLoaded = False
        
        
    def getValue(self, section_str, key_str):
        if self.configFileLoaded == True:
            if section_str in self.sections:
                return self.parser[section_str][key_str]
            
    
    def hasConfigData(self):
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
        if os.path.exists(self.config_file):
            self.parser.read(self.config_file)
            self.configFileLoaded = True  
 
        