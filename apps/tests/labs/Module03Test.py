import unittest


"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module03 import SensorDataManager, TempActuatorAdapter, TempSensorAdapter, TempSensorAdapterTask
from labs.common import SensorData
class Module03Test(unittest.TestCase):

	"""
	UnitTests for
	- SensorDataManager
	- TempActuatorAdapter
	- TempSensorAdapter
	"""
	def setUp(self):
		self.sensorDataManagerTest          = SensorDataManager.SensorDataManager()
		#self.tempSensorAdapterTest   = TempSensorAdapter.TempSensorAdapter()
		#self.tempActuatorAdapterTest = TempActuatorAdapter.TempActuatorAdapter()
		#self.tempSensorAdapterTaskTest   = TempSensorAdapterTask.TempSensorAdapterTask()
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
	Testing the testUpdateActuator function in SensorDataManager
	'''
	def testUpdateActuator(self):
		
		pass

	def testClear(self):
		pass
	
	def testRunTempAdapter(self):
		pass

	def testReadTemperature(self):
		pass

	def testGenerateString(self):
		pass
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()