import unittest
from labs.common import SensorData
from labs.module02 import TempSensorEmulatorTask

class SensorDataTest(unittest.TestCase):

	def setUp(self):
		self.SensorDataTests = SensorData.SensorData()
		pass

	def tearDown(self):
		pass
	
	"""
	Place your comments describing the test here.
	"""
	def testAddValue(self):
		print("\n")
		self.assertEqual(True, self.SensorDataTests.addValue(6.0),"Float Value Added")
		self.assertEqual(False, self.SensorDataTests.addValue("NOTAFLOAT"))
		pass

	def testGetAverageValue(self):
		print("\n")
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.SensorDataTests.addValue(3.2)
		self.assertEqual(6.5,self.SensorDataTests.getAverageValue())

		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(6.5,self.SensorDataTests.getAverageValue())

		pass
	
	def testGetCount(self):
		print("\n")
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.assertEqual(2,self.SensorDataTests.getCount())

		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(2,self.SensorDataTests.getCount())
		pass
	
	def testGetCurrentValue(self):
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.assertEqual(10.3,self.SensorDataTests.getCurrentValue())

		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(10.3,self.SensorDataTests.getCurrentValue())
		pass

	def testGetMaxValue(self):
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.assertEqual(10.3,self.SensorDataTests.getMaxValue())

		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(10.3,self.SensorDataTests.getMaxValue())
		pass

	def testGetMinValue(self):
		self.SensorDataTests.addValue(6.0)
		self.SensorDataTests.addValue(10.3)
		self.SensorDataTests.addValue(8.8)
		self.assertEqual(6.0,self.SensorDataTests.getMinValue())

		self.SensorDataTests.addValue("NOTAFLOAT")
		self.assertEqual(6.0,self.SensorDataTests.getMinValue())
		pass

	def testGetName(self):
		self.assertEqual("Not Set", self.SensorDataTests.getName())
		self.SensorDataTests.setName("TESTNAME")
		self.assertEqual("TESTNAME", self.SensorDataTests.getName())
		pass

	def testSetName(self):
		self.SensorDataTests.setName("TESTNAME")
		self.assertEqual("TESTNAME", self.SensorDataTests.getName())
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()