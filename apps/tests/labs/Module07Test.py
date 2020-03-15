import unittest

from labs.module07 import MultiActuatorAdapter, MultiSensorAdapter, TempSensorAdapterTask, CoAPClientConnector
from labs.common import SensorData, ActuatorData, PersistenceUtil, ActuatorDataListener
import redis
import asyncio
from time import sleep

class Module07Test(unittest.TestCase):

	"""
	Setting up resources 
	"""
	def setUp(self):
		#Setting up resources from common
		#Creating PersistenceUtil object
		self.pUtil = PersistenceUtil.PersistenceUtil()
		#Instances from Module06
		self.coAPTest = CoAPClientConnector.CoAPClientConnector()
		self.multiActuatorAdapterTest = MultiActuatorAdapter.MultiActuatorAdapter()
		self.tempSensorAdapterTaskTest = TempSensorAdapterTask.TempSensorAdapterTask(1,1,self.pUtil,self.coAPTest)
		self.multiSensorAdapterTest = MultiSensorAdapter.MultiSensorAdapter(1,1)
		#Getting an asyncio event loop
		self.loop = asyncio.get_event_loop()
		#SensorData object
		self.sensorData = SensorData.SensorData()
		self.sensorData.addValue(10)
		self.sensorData.setName("TESTNAME")
		#ActuatorData object
		self.actuatorData = ActuatorData.ActuatorData()
		self.actuatorData.setCommand("TESTCOMMAND")
		self.actuatorData.setValue("TESTVALUE")
		self.actuatorData.setName("TESTNAME")
		

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.MultiActuatorAdapterTest = None
		self.tempSensorAdapterTaskTest = None
		self.multiSensorAdapterTest = None
		self.actuatorData = None
		self.sensorData =

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
	Testing registerActuatorDataListener in CoAPClientConnector
	'''	
	def testregisterActuatorDataListener(self):
		#Should return True when right input
		self.assertEqual(True,self.coAPTest.registerActuatorDataListener(ActuatorDataListener.ActuatorDataListener(redis.Redis)))
		#Should return False when wrong input
		self.assertEqual(False,self.coAPTest.registerActuatorDataListener(object))
	
	'''
	Testing dataPUT in CoAPClientConnector
	'''	
	def testDataPUT(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataPUT("TEST STRING")))

	'''
	Testing dataPOST in CoAPClientConnector
	'''	
	def testDataPOST(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataPOST("TEST STRING")))
	
	'''
	Testing dataGET in CoAPClientConnector
	'''	
	def testDataGET(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataGET()))

	'''
	Testing dataDelete in CoAPClientConnector
	'''	
	def testDataDelete(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataDelete()))

	'''
	Testing getData in CoAPClientConnector
	'''
	def testGetData(self):
		#Should always return a True
		self.assertEqual(True,self.coAPTest.getData(self.loop))
	
	'''
	Testing deleteData in CoAPClientConnector
	'''
	def testDeleteData(self):
		#Should always return a True
		self.assertEqual(True,self.coAPTest.deleteData(self.loop))

	'''
	Testing sendSensorDataPUT in CoAPClientConnector
	'''
	def testSendSensorDataPUT(self):
		#Should return false when input not SensorData
		self.assertEqual(False,self.coAPTest.sendSensorDataPUT(self.loop,object))
		#Should return true when input is SensorData
		self.assertEqual(True,self.coAPTest.sendSensorDataPUT(self.loop,self.sensorData))
	
	'''
	Testing sendSensorDataPOST in CoAPClientConnector
	'''
	def testSendSensorDataPOST(self):
		#Should return false when input not SensorData
		self.assertEqual(False,self.coAPTest.sendSensorDataPOST(self.loop,object))
		#Should return true when input is SensorData
		self.assertEqual(True,self.coAPTest.sendSensorDataPOST(self.loop,self.sensorData))
	

		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()