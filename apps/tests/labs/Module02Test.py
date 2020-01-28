import unittest


"""
Test class for all requisite Module02 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module02 import ConfigUtil, SensorData, SmtpClientConnector, TempEmulatorAdapter, TempSensorEmulatorTask
class Module02Test(unittest.TestCase):

	def setUp(self):
		self.configUtilTests = ConfigUtil.ConfigUtil()
		pass

	def tearDown(self):
		pass
	
	def testGetValue(self):
		pass

	def testHasConfigData(self):
		testBoolean = self.configUtilTests.hasConfigData()
		self.assertTrue(type(testBoolean) == bool,"HasConfigData returned a non boolean value")
	
	def testLoadConfigData(self):
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()