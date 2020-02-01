import unittest
from labs.common import SensorData
from labs.module02 import TempSensorEmulatorTask

class SensorDataTest(unittest.TestCase):
	'''
    Test class for SensorData functionality.
    '''
	def setUp(self):
		#get a sensorData instance
		self.SensorDataTests = SensorData.SensorData()
		pass

	def tearDown(self):
		pass
	
	'''
	Testing the addValue method
	'''
	def testAddValue(self):
		print("\n")
		#Checking if a float value could be added
		self.assertEqual(True, self.SensorDataTests.addValue(6.0),)
		#Checking when a non float value is passed
		self.assertEqual(False, self.SensorDataTests.addValue("NOTAFLOAT"))
		pass
	'''
	Testing the getAverageValue method
	'''
	def testGetAverageValue(self):
		print("\n")
		#Checking if a series of float value could be added
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.SensorDataTests.addValue(3.2)
		#Checking if it returns the correct averageValue
		self.assertEqual(6.5,self.SensorDataTests.getAverageValue())
		#Checking when a non float value is passed
		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(6.5,self.SensorDataTests.getAverageValue())
		pass
	'''
	Testing the getCount method
	'''
	def testGetCount(self):
		print("\n")
		#Checking if a series of float value could be added
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		#Checking if it returns the correct count
		self.assertEqual(2,self.SensorDataTests.getCount())
		#Checking when a non float value is passed
		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(2,self.SensorDataTests.getCount())
		pass
	'''
	Testing the getCount method
	'''
	def testGetCurrentValue(self):
		print("\n")
		#Checking if a series of float value could be added
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		#Checking if it returns the correct CurrentValue
		self.assertEqual(10.3,self.SensorDataTests.getCurrentValue())
		#Checking when a non float value is passed
		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(10.3,self.SensorDataTests.getCurrentValue())
		pass
	'''
	Testing the getMaxValue method
	'''
	def testGetMaxValue(self):
		print("\n")
		#Checking if a series of float value could be added
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		#Checking if it returns the correct MaxValue
		self.assertEqual(10.3,self.SensorDataTests.getMaxValue())
		#Checking when a non float value is passed
		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(10.3,self.SensorDataTests.getMaxValue())
		pass
	'''
	Testing the getMinValue method
	'''
	def testGetMinValue(self):
		print("\n")
		#Checking if a series of float value could be added
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.SensorDataTests.addValue(8.8)
		#Checking if it returns the correct MinValue
		self.assertEqual(6.0,self.SensorDataTests.getMinValue())
		#Checking when a non float value is passed
		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(6.0,self.SensorDataTests.getMinValue())
		pass
	'''
	Testing the getName method
	'''
	def testGetName(self):
		print("\n")
		#Checking the getName returns the correct name
		self.assertEqual("Not Set", self.SensorDataTests.getName())
		#Checking the getName returns the correct name after setting a new name
		self.SensorDataTests.setName("TESTNAME")
		self.assertEqual("TESTNAME", self.SensorDataTests.getName())
		pass
	'''
	Testing the setName method
	'''
	def testSetName(self):
		print("\n")
		#Checking the getName returns the correct name after setting a new name using setName
		self.SensorDataTests.setName("TESTNAME")
		self.assertEqual("TESTNAME", self.SensorDataTests.getName())
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()