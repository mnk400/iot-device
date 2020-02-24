import unittest
from labs.common import ActuatorData, SensorData, PersistenceUtil
from os import path
class PersistenceUtilTest(unittest.TestCase):
    """
    Testing the 4 methods from PersistenceUtil Class
    """

    """
    Setting up resources
    """
    def setUp(self):
        #Instance for persistenceUtil
        self.pUtil = PersistenceUtil.PersistenceUtil()
        self.pUtil.enableThreads = False
        #ActuatorData instance filled with data
        self.actuatorData = ActuatorData.ActuatorData()
        self.actuatorData.setName("TestActuator")
        self.actuatorData.setCommand("TestCommand")
        self.actuatorData.setValue("TestValue")
        #SensorData instance filled with data
        self.sensorData = SensorData.SensorData()
        self.sensorData.setName("TestSensor")
        self.sensorData.addValue(10)
        #Creating a variable to avoid running this pipeline in cloud
        if path.exists("config/ConnectedDevicesConfig.props"):
            self.pipelineAvoid = False
        else:
            self.pipelineAvoid = True 
        
    """
    Getting rid of resources
    """
    def tearDown(self):
        self.actuatorData = None
        self.sensorData = None   

    '''
    Testing method which registers the listener thread for actuatorData
    '''
    def testRegisterActuatorDataDbmsListener(self):
        #Running only certain tests in pipeline
        #but all the tests when locally 
        if self.pipelineAvoid == False:
            #Checking true when thread should've ran
            self.assertEqual(True,self.pUtil.registerActuatorDataDbmsListener())
            #When thread should'nt've ran
            self.pUtil.connected = False
            self.assertEqual(False,self.pUtil.registerActuatorDataDbmsListener())
        #when in pipeline    
        else:
            self.assertEqual(False,self.pUtil.registerActuatorDataDbmsListener())

    '''
    Testing method which registers the listener thread for sensorData
    '''
    def testRegisterSensorDataDbmsListene(self):
        
        #Running only certain tests in pipeline
        #but all the tests when locally 
        if self.pipelineAvoid == False:
            #Checking true when thread should've ran
            self.assertEqual(True,self.pUtil.registerSensorDataDbmsListener())
            #When thread should'nt've ran
            self.pUtil.connected = False
            self.assertEqual(False,self.pUtil.registerSensorDataDbmsListener())
        #when in pipeline    
        else:
            self.assertEqual(False,self.pUtil.registerSensorDataDbmsListener())
  

    '''
    Testing method which writes sensorData to redis 
    '''
    def testWriteSensorDataDbmsListener(self):     
        #Running only certain tests in pipeline
        #but all the tests when locally 
        if self.pipelineAvoid == False:
            #Checking true when thread should've ran
            self.assertEqual(True,self.pUtil.writeSensorDataDbmsListener(self.sensorData))
            #When thread should'nt've ran
            self.pUtil.connected = False
            self.assertEqual(False,self.pUtil.writeSensorDataDbmsListener(self.sensorData))
        #when in pipeline    
        else:
            self.assertEqual(False,self.pUtil.writeSensorDataDbmsListener(self.sensorData))

    '''
    Testing method which writes actuatorData to redis 
    '''
    def testWriteActuatorDataDbmsListener(self):  
        #Running only certain tests in pipeline
        #but all the tests when locally 
        if self.pipelineAvoid == False:
            #Checking true when thread should've ran
            self.assertEqual(True,self.pUtil.writeActuatorDataDbmsListener(self.actuatorData))
            #When thread should'nt've ran
            self.pUtil.connected = False
            self.assertEqual(False,self.pUtil.writeActuatorDataDbmsListener(self.actuatorData))
        #when in pipeline    
        else:
            self.assertEqual(False,self.pUtil.writeActuatorDataDbmsListener(self.actuatorData))  

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()