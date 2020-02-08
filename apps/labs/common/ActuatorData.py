'''
Created on Feb 6, 2020

@author: manik
'''

class ActuatorData(object):
    '''
    ActuatorData class which stores the current state of the actuator
    Has a certain functions to set and get data.
    '''

    def __init__(self):
        '''
        Constructor
        Initialize the variables as 'Not Set' and 0.0.
        '''
        self.command = "Not Set"
        self.name = "Not Set"
        self.value = None
        pass
    
    def getCommand(self) -> str:
        '''
        Function to return the current set command for the actuator.
        '''
        return self.command

    def getName(self) -> str:
        '''
        Function the name of current ActuatorData instance if set.
        '''
        return self.name

    def getValue(self) -> float:
        '''
        Function to return the current set value of the instance.
        '''
        return self.value

    def setCommand(self, input_command) -> bool:
        '''
        Function to set or change the current set command for the actuator.
        '''
        self.command = input_command
        return True

    def setName(self, name_param) -> bool:
        '''
        Function to set the name of the instance.
        '''
        self.name = name_param
        return True
    
    def setValue(self, value_param):
        '''
        Function to set the value of the actuator.
        '''
        self.value = value_param
        return True