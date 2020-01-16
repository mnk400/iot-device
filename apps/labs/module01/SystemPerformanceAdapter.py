'''
Created on Jan 15, 2020

@author: manik
'''
import logging

from labs.module01      import SystemCpuUtilTask, SystemMemUtilTask
from time               import sleep

logging.getLogger("adapterlog")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG) 
logging.info("System Performance Thread initializing")


class SystemPerformanceAdapter(object):

    def __init__(self,param):
        '''
        Constructor
        '''
        self.sleeptime = param
    
        
    def run(self,param):
        '''
        Method to log the current CPU and Memory usage
        '''
        cpu = SystemCpuUtilTask.Cpu()
        mem = SystemMemUtilTask.Mem()
        i = 0
        while i < param:
            cpuval = cpu.getDataFromSensor()
            memval = mem.getDataFromSensor()
            logging.info('CPU Utilization=' + str(cpuval))
            logging.info('Memory Utilization=' + str(memval))
            sleep(self.sleeptime)
            i = i + 1