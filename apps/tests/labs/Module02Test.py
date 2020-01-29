import unittest

from labs.module02 import ConfigUtil, SensorData, SmtpClientConnector, TempEmulatorAdapter, TempSensorEmulatorTask
class Module02Test(unittest.TestCase):

	def setUp(self):
		self.configUtilTests = ConfigUtil.ConfigUtil()
		pass

	def tearDown(self):
		pass
	
	def testGetValue(self):
		pass

	'''
	Testing if the config file is loading data from the file properly
	'''
	def testHasConfigData(self):
		testBoolean = self.configUtilTests.hasConfigData()
		self.assertTrue(type(testBoolean) == bool,"HasConfigData returned a non boolean value")
	'''
	Test for if the method that checks if config data has been
	loaded works as it intended to
	'''
	def testLoadConfigData(self):
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()