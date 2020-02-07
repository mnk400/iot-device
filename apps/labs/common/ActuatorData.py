'''
Created on Feb 6, 2020

@author: manik
'''

class ActuatorData(object):
    '''
    Classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.command = "Not Set"
        self.name = "Not Set"
        self.value = 0.0
        pass
    
    def getCommand(self):
        return self.command

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def setCommand(self, input_command):
        self.command = input_command

    def setName(self, name_param):
        self.name = name_param