import unittest

from labs.common import ConfigUtil
class ConfigUtilTest(unittest.TestCase):
	'''
	Unittest for the ConfigUtil
	'''
	def setUp(self):
		'''
		Setting up required resources
		'''
		self.configUtilTests = ConfigUtil.ConfigUtil()
		self.configUtilTests.loadConfigData()
		#The following case is for the github/gitbucket pipeline where the real config file is not pushed hence the tests are performed using a SAMPLE
		if self.configUtilTests.configFileLoaded == False:
			#loading the sample config file
			self.configUtilTests.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")
			self.configUtilTests.loadConfigData()
		pass

	def tearDown(self):
		self.configUtilTests = None
		pass
	
	"""
	Tests retrieval of a boolean property.
	"""
	def testGetBooleanProperty(self):
		print("\n")
		#tesing when the key is a Boolean, should return a true
		self.assertEqual(True, self.configUtilTests.getBooleanValue("ubidots.cloud","useWebAccess"))
		#testing when the key is not a boolean, should return a none
		self.assertEqual(None, self.configUtilTests.getBooleanValue("smtp.cloud","host"))
		#testing when random values are passed into section and key, should expect a none
		self.assertEqual(None, self.configUtilTests.getBooleanValue("randomVal","randomKey"))
		pass
	
	"""
	Tests retrieval of an integer property.
	"""
	def testGetIntegerProperty(self):
		print("\n")
		#testing when the key is a Integer, should return an int
		self.assertEqual(465, self.configUtilTests.getIntegerValue("smtp.cloud","port"))
		#testing when the key is not a Integer, should return a false
		self.assertEqual(False, self.configUtilTests.getIntegerValue("ubidots.cloud","host"))
		#testing when random values are passed into section and key, should expect a false
		self.assertEqual(False, self.configUtilTests.getIntegerValue("randomVal","randomKey"))
		pass
	
	"""
	Tests retrieval of a string property.
	"""
	def testGetProperty(self):
		print("\n")
		#testing when the key is a string, should return the same string
		self.assertEqual("test.mosquitto.org", self.configUtilTests.getValue("mqtt.cloud","host"))
		#testing when the key is not a String, should expect a string
		self.assertEqual("127.0.0.1", self.configUtilTests.getValue("coap.cloud","host"))
        #testing when random values are passed into section and key, should expect a false
		self.assertEqual(False, self.configUtilTests.getValue("randomVal","randomKey"))
		pass
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		print("\n")
		#testing getValue when a key is asked for that doesn't exist
		self.assertEqual(False, self.configUtilTests.getValue("mqtt.cloud","WRONGKEY"))
		#testing getIntegerValue when a key is asked for that doesn't exist
		self.assertEqual(False, self.configUtilTests.getIntegerValue("ubidot.cloud","WRONGKEY"))
		#testing getBooleanValue when a key is asked for that doesn't exist
		self.assertEqual(None, self.configUtilTests.getBooleanValue("coap.cloud","WRONGKEY"))
		pass

	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		print("\n")
		#testing getValue when a section is asked for that doesn't exist
		self.assertEqual(False, self.configUtilTests.getValue("WRONGSECTION","hosts"))
		#testing getIntegerValue when a section is asked for that doesn't exist
		self.assertEqual(False, self.configUtilTests.getIntegerValue("WRONGSECTION","hosts"))
		#testing getBooleanValue when a section is asked for that doesn't exist
		self.assertEqual(None, self.configUtilTests.getBooleanValue("WRONGSECTION","WRONGKEY"))
		pass
	
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		#checking if the config file has been loaded, when the path is correct
		self.assertEqual(True, self.configUtilTests.loadConfigData())
		#checking if the config file has been loaded, when the path is wrong
		self.configUtilTests = ConfigUtil.ConfigUtil("/path/to/somewhere/else.props")
		self.assertEqual(False, self.configUtilTests.loadConfigData())
		pass
	
if __name__ == "__main__":
	unittest.main()
