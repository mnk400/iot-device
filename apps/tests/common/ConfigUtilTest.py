import unittest

from labs.common import ConfigUtil
class ConfigUtilTest(unittest.TestCase):

	def setUp(self):
		self.configUtilTests = ConfigUtil.ConfigUtil()
		#self.configUtilTests.loadConfigData()
		if self.configUtilTests.configFileLoaded == False:
			self.configUtilTests.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")
			self.configUtilTests.loadConfigData()
		pass

	def tearDown(self):
		pass
	
	"""
	Tests retrieval of a boolean property.
	"""
	def testGetBooleanProperty(self):

		self.assertEqual(True, self.configUtilTests.getBooleanValue("ubidots.cloud","useWebAccess"))
		
		self.assertEqual(None, self.configUtilTests.getBooleanValue("smtp.cloud","host"))

		self.assertEqual(None, self.configUtilTests.getBooleanValue("randomVal","randomKey"))
		pass
	
	"""
	Tests retrieval of an integer property.
	"""
	def testGetIntegerProperty(self):
		print("\n")
		self.assertEqual(465, self.configUtilTests.getIntegerValue("smtp.cloud","port"))
		
		self.assertEqual(False, self.configUtilTests.getIntegerValue("ubidots.cloud","host"))

		self.assertEqual(False, self.configUtilTests.getIntegerValue("randomVal","randomKey"))
		pass
	
	"""
	Tests retrieval of a string property.
	"""
	def testGetProperty(self):
		print("\n")
		self.assertEqual("test.mosquitto.org", self.configUtilTests.getValue("mqtt.cloud","host"))
		
		self.assertEqual("127.0.0.1", self.configUtilTests.getValue("coap.cloud","host"))

		self.assertEqual(False, self.configUtilTests.getValue("randomVal","randomKey"))
		pass
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		print("\n")
		self.assertEqual(False, self.configUtilTests.getValue("mqtt.cloud","WRONGKEY"))
		self.assertEqual(False, self.configUtilTests.getIntegerValue("ubidot.cloud","WRONGKEY"))
		self.assertEqual(None, self.configUtilTests.getBooleanValue("coap.cloud","WRONGKEY"))
		pass

	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		print("\n")
		self.assertEqual(False, self.configUtilTests.getValue("WRONGSECTION","hosts"))
		self.assertEqual(False, self.configUtilTests.getIntegerValue("WRONGSECTION","hosts"))
		self.assertEqual(None, self.configUtilTests.getBooleanValue("WRONGSECTION","WRONGKEY"))
		pass
	
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		self.assertEqual(True, self.configUtilTests.loadConfigData())
		self.configUtilTests = ConfigUtil.ConfigUtil("/path/to/somewhere/else.props")
		self.assertEqual(False, self.configUtilTests.loadConfigData())
		pass
	
	def testHasConfigData(self):
		pass
	
if __name__ == "__main__":
	unittest.main()
