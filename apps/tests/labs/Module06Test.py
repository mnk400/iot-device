import unittest
from os import path
from labs.module06 import MultiActuatorAdapter, MultiSensorAdapter, TempSensorAdapterTask, MqttClientConnector
from labs.common import SensorData, ActuatorData
from time import sleep
class Module06Test(unittest.TestCase):

	"""
	Setting up resources 
	"""
	def setUp(self):
		#Setting up resources from common
		self.mqttTest = MqttClientConnector.MqttClientConnector()
		self.multiActuatorAdapterTest = MultiActuatorAdapter.MultiActuatorAdapter()
		self.tempSensorAdapterTaskTest = TempSensorAdapterTask.TempSensorAdapterTask(1,1,self.mqttTest)
		self.multiSensorAdapterTest = MultiSensorAdapter.MultiSensorAdapter(1,1)
		#SensorData object
		self.sensorData = SensorData.SensorData()
		self.sensorData.addValue(10)
		self.sensorData.setName("TESTNAME")
		#ActuatorData object
		self.actuatorData = ActuatorData.ActuatorData()
		self.actuatorData.setCommand("TESTCOMMAND")
		self.actuatorData.setValue("TESTVALUE")
		self.actuatorData.setName("TESTNAME")
		#Variable to avoid in pipeline
		if path.exists("config/ConnectedDevicesConfig.props"):
			self.run = False
		else:
			self.run = True
		

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.MultiActuatorAdapterTest = None
		self.tempSensorAdapterTaskTest = None
		self.multiSensorAdapterTest = None
	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testUpdateActuator(self):
		#Creating a temporary actuatorData instance
		actuator = ActuatorData.ActuatorData()
		actuator.setCommand("Print")
		actuator.setValue(["TEST",(90,200,90)])
		#Checking for a compatible command
		self.assertEqual(True,self.multiActuatorAdapterTest.updateActuator(actuator))
		#Checking for an incompatible command
		actuator.setCommand("This shouldn't work")
		self.assertEqual(False,self.multiActuatorAdapterTest.updateActuator(actuator))
		self.multiActuatorAdapterTest.clear()

	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testClear(self):
		#Testing the clear function
		self.assertEqual(True,self.multiActuatorAdapterTest.clear())

	'''
	Testing the run function in TempSensorAdapterTask
	'''
	def testRun(self):
		#Should always return a True, no matter what the parameters
		self.assertEqual(True, self.tempSensorAdapterTaskTest.run())


	'''
	Testing the run function in TempSensorAdapterTask
	'''
	def test__init__threads__(self):
		#Testing the function which runs threads
		#Should not run when setting disabled and return False
		self.multiSensorAdapterTest.enableTempTask = False
		self.assertEqual(False,self.multiSensorAdapterTest.__init_threads__())
		self.multiSensorAdapterTest.enableTempTask = True
		#Should run when setting is enabled
		self.assertEqual(True,self.multiSensorAdapterTest.__init_threads__())

	'''
	Testing the testGenerateString function in TempSensorAdapterTask
	'''
	def testGenerateString(self):
		#Should return an object of type string
		self.tempSensorAdapterTaskTest.sensorData.addValue(20)
		self.assertEqual(str, type(self.tempSensorAdapterTaskTest.generateString()))

	'''
	Testing PublishActuatorData in MqttClientConnector
	'''	
	def testPublishActuatorData(self):
		#Testing case when wrong input
		tempObj = object()
		self.assertEqual(False,self.mqttTest.publishActuatorData(tempObj))
		#Testing when the connected is False
		self.assertEqual(False,self.mqttTest.publishActuatorData(self.actuatorData))
		#Testing when connected, not running this in the pipeline, should return true
		self.mqttTest.connectActuatorData()
		self.assertEqual(False,self.mqttTest.publishActuatorData(self.actuatorData))
		

	'''
	Testing PublishSensorData in MqttClientConnector
	'''	
	def testPublishSensorData(self):
		#Testing case when wrong input
		tempObj = object()
		self.assertEqual(False,self.mqttTest.publishSensorData(tempObj))
		#Testing when the connected is False
		self.assertEqual(False,self.mqttTest.publishSensorData(self.sensorData))
		#Testing when connected, not running this in the pipeline, should return a True
		self.mqttTest.connectSensorData()
		self.assertEqual(False,self.mqttTest.publishSensorData(self.sensorData))

	'''
	Testing ConnectActuatorData in MqttClientConnector
	'''	
	def testConnectActuatorData(self):
		#Should always return true
		self.assertEqual(True,self.mqttTest.connectActuatorData())


	'''
	Testing ConnectSensorData in MqttClientConnector
	'''	
	def testConnectSensorData(self):
		#Should always return true
		self.assertEqual(True,self.mqttTest.connectSensorData())


	'''
	Testing ListenActuatorData in MqttClientConnector
	'''	
	def testListenActuatorData(self):
		#Should return a false when not connected
		self.assertEqual(False,self.mqttTest.listenActuatorData())
		#Should return a true when connected
		self.mqttTest.connectActuatorData()
		sleep(1)
		self.assertEqual(True,self.mqttTest.listenActuatorData())
		self.mqttTest.disconnect()
		

	'''
	Testing ListenSensorData in MqttClientConnector
	'''	
	def testListenSensorData(self):
		#Should return a false when not connected
		self.assertEqual(False,self.mqttTest.listenSensorData())
		#Should return a true when connected
		self.mqttTest.connectSensorData()
		sleep(1)
		self.assertEqual(True,self.mqttTest.listenSensorData())
		self.mqttTest.disconnect()
		


		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()