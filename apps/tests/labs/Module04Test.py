import unittest
import numpy
from labs.module04 import SensorDataManager, MultiActuatorAdapter, MultiSensorAdapter, HI2CSensorAdapterTask, HumiditySensorAdapterTask
from labs.common import SensorData, ActuatorData

"""
TestCases for python files in Module04
"""
class Module04Test(unittest.TestCase):

	"""
	UnitTests for
	- SensorDataManager
	- TempActuatorAdapter
	- TempSensorAdapter
	- TempSensorAdapterTask
	"""
	def setUp(self):
		self.SensorDataManagerTest         = SensorDataManager.SensorDataManager()
		self.HI2CSensorAdapterTaskTest     = HI2CSensorAdapterTask.HI2CSensorAdapterTask(1,1)
		self.HumiditySensorAdapterTaskTest = HumiditySensorAdapterTask.HumiditySensorAdapterTask(1,1)
		self.MultiActuatorAdapterTest      = MultiActuatorAdapter.MultiActuatorAdapter()
		self.MultiSensorAdapterTest		   = MultiSensorAdapter.MultiSensorAdapter(1, 1, 1, 1)
		pass

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		#self.SensorDataTest = None
		#self.tempSensorAdapterTask = None
		#self.tempActuatorAdapterTest = None
		#self.tempSensorAdapterTaskTest = None
		pass

	'''
	Testing the handleSensorData function in SensorDataManager
	'''
	def testHandleSensorData(self):
		#Creating a temporary sensorData instance
		sensor = SensorData.SensorData()
		sensor.addValue(20)
		self.SensorDataManagerTest.SEND_EMAIL_NOTIFICATION = False
		#Calling the test handleSensorData function, should return true if worked properly
		self.assertEqual(True,self.SensorDataManagerTest.handleSensorData(sensor, "testMessage"))
		#Passing any other generic object will render a False result
		obj = object()
		self.assertEqual(False,self.SensorDataManagerTest.handleSensorData(obj,"no"))
		pass

	'''
	Testing the testSendNotification function in SensorDataManager
	'''
	def testSendNotification(self):
		#Running the tests if configFile is loaded, so that we can avoid with a 
		#failing build in cloud.
		if self.SensorDataManagerTest.config.configFileLoaded == True:
			self.assertEqual(True, self.SensorDataManagerTest.sendNotification("Test message sent from sendNotification.sensorDataManager"))
		#Checking if the email notification switch works
		#Should not sent Email in this case
		self.SensorDataManagerTest.SEND_EMAIL_NOTIFICATION = False
		self.assertEqual(True, self.SensorDataManagerTest.sendNotification("Should not send"))
		pass

	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testUpdateActuator(self):
		#Creating a temporary actuatorData instance
		actuator = ActuatorData.ActuatorData()
		actuator.setCommand("Increase")
		actuator.setValue(self.SensorDataManagerTest.STABLE)
		#Checking for a compatible command
		self.assertEqual(True,self.MultiActuatorAdapterTest.updateActuator(actuator))
		#Checking for an incompatible command
		actuator.setCommand("This shouldn't work")
		self.assertEqual(False,self.MultiActuatorAdapterTest.updateActuator(actuator))
		self.MultiActuatorAdapterTest.clear()
		pass

	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testClear(self):
		#testing the clear function
		self.assertEqual(True,self.MultiActuatorAdapterTest.clear())
		pass
	
	'''
	Testing the RunAdapter function in MultiSensorAdapter
	'''
	def testRunTempAdapter(self):
		#Function should return a True if ran properly
		#Disabling the sendEmail setting just cause
		self.MultiSensorAdapterTest.sendEmail = False
		self.assertEqual(True,self.MultiSensorAdapterTest.runAdapter())
		pass
	
	'''
	Testing the Run function in HI2CSensorAdapterTask
	'''
	def testRunHI2C(self):
		#Should return a True if ran properly
		self.HI2CSensorAdapterTaskTest.sensorDataManager.SEND_EMAIL_NOTIFICATION = False
		self.assertEqual(True,self.HI2CSensorAdapterTaskTest.run())
		pass

	'''
	Testing the GenerateString function in HI2CSensorAdapterTask
	'''
	def testGenerateStringHI2C(self):
		#Should return an object of type string
		self.HI2CSensorAdapterTaskTest.sensor_data.addValue(20)
		self.assertEqual(str, type(self.HI2CSensorAdapterTaskTest.generateString()))
		pass
	
	'''
	Testing the ParseI2CData function in HI2CSensorAdapterTask
	'''
	def testParseI2CData(self):
		self.assertEqual(numpy.float64,type(self.HI2CSensorAdapterTaskTest.parseI2CData()))
		pass
	
	'''
	Testing the InitI2CBus function in HI2CSensorAdapterTask
	'''
	def testInitI2CBus(self):
		self.assertEqual(True, self.HI2CSensorAdapterTaskTest.initI2CBus())
	'''
	Testing the Run function in HumiditySensorAdapterTask
	'''
	def testRunHumidity(self):
		#Should return a True if ran properly
		self.HumiditySensorAdapterTaskTest.sensorDataManager.SEND_EMAIL_NOTIFICATION = False
		self.assertEqual(True,self.HumiditySensorAdapterTaskTest.run())
		pass

	'''
	Testing the GenerateString function in HumiditySensorAdapterTask
	'''
	def testGenerateStringHumidity(self):
		#Should return an object of type string
		self.HumiditySensorAdapterTaskTest.sensor_data.addValue(20)
		self.assertEqual(str, type(self.HumiditySensorAdapterTaskTest.generateString()))
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()