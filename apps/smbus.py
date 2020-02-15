'''
Created on Feb 14, 2020

@author: manik
Created for passing random values in SMBus methods
'''

from random import randint

class SMBus(object):
    
    def __init__(self, a):
        pass

    def write_byte_data(self, a, b, c) -> bool:
        return True

    def read_byte_data(self, a, b) -> float:
        value = randint(0, 10)
        return value