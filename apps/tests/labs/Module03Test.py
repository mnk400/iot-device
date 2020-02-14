import unittest


"""
TestCases for python files in Module03
"""
from labs.module03 import SensorDataManager, TempActuatorAdapter, TempSensorAdapter, TempSensorAdapterTask
from labs.common import SensorData, ActuatorData

class Module03Test(unittest.TestCase):

	"""
	UnitTests for
	- SensorDataManager
	- TempActuatorAdapter
	- TempSensorAdapter
	- TempSensorAdapterTask
	"""
	def setUp(self):
		self.sensorDataManagerTest     = SensorDataManager.SensorDataManager()
		self.tempSensorAdapterTest     = TempSensorAdapter.TempSensorAdapter()
		self.tempActuatorAdapterTest   = TempActuatorAdapter.TempActuatorAdapter()
		self.tempSensorAdapterTaskTest = TempSensorAdapterTask.TempSensorAdapterTask()
		
		pass

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.sensorDataTest = None
		self.tempSensorAdapterTask = None
		self.tempActuatorAdapterTest = None
		self.tempSensorAdapterTaskTest = None
		pass

	'''
	Testing the handleSensorData function in SensorDataManager
	'''
	def testHandleSensorData(self):
		#Creating a temporary sensorData instance
		sensor = SensorData.SensorData()
		sensor.addValue(20)
		self.sensorDataManagerTest.SEND_EMAIL_NOTIFICATION = False
		#Calling the test handleSensorData function, should return true if worked properly
		self.assertEqual(True,self.sensorDataManagerTest.handleSensorData(sensor, "testMessage"))
		#Passing any other generic object will render a False result
		obj = object()
		self.assertEqual(False,self.sensorDataManagerTest.handleSensorData(obj,"no"))
		pass

	'''
	Testing the testSendNotification function in SensorDataManager
	'''
	def testSendNotification(self):
		#Running the tests if configFile is loaded, so that we can avoid with a 
		#failing build in cloud.
		if self.sensorDataManagerTest.config.configFileLoaded == True:
			self.assertEqual(True, self.sensorDataManagerTest.sendNotification("Test message sent from sendNotification.sensorDataManager"))
		#Checking if the email notification switch works
		#Should not sent Email in this case
		self.sensorDataManagerTest.SEND_EMAIL_NOTIFICATION = False
		self.assertEqual(True, self.sensorDataManagerTest.sendNotification("Should not send"))
		pass

	'''
	Testing the testUpdateActuator function in TempActuatorAdapter
	'''
	def testUpdateActuator(self):
		#Creating a temporary actuatorData instance
		actuator = ActuatorData.ActuatorData()
		actuator.setCommand("Increase")
		actuator.setValue(self.sensorDataManagerTest.STABLE)
		#Checking for a compatible command
		self.assertEqual(True,self.tempActuatorAdapterTest.updateActuator(actuator))
		#Checking for an incompatible command
		actuator.setCommand("This shouldn't work")
		self.assertEqual(False,self.tempActuatorAdapterTest.updateActuator(actuator))
		self.tempActuatorAdapterTest.clear()
		pass

	'''
	Testing the testUpdateActuator function in TempActuatorAdapter
	'''
	def testClear(self):
		#testing the clear function
		self.assertEqual(True,self.tempActuatorAdapterTest.clear())
		pass
	
	'''
	Testing the testRunTempAdapter function in TempSensorAdapter
	'''
	def testRunTempAdapter(self):
		#Function should return a True if ran properly
		#Disabling the sendEmail setting just cause
		self.tempSensorAdapterTest.sendEmail = False
		self.assertEqual(True,self.tempSensorAdapterTest.run_temp_adapter())
		pass
	
	'''
	Testing the testReadTemperature function in TempSensorAdapterTask
	'''
	def testReadTemperature(self):
		#Should return a True if ran properly
		self.tempSensorAdapterTaskTest.sensorDataManager.SEND_EMAIL_NOTIFICATION = False
		self.assertEqual(True,self.tempSensorAdapterTaskTest.readTemperature())
		pass
	
	'''
	Testing the testGenerateString function in TempSensorAdapterTask
	'''
	def testGenerateString(self):
		#Should return an object of type string
		self.tempSensorAdapterTaskTest.sensor_data.addValue(20)
		self.assertEqual(str, type(self.tempSensorAdapterTaskTest.generateString()))
		pass
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()