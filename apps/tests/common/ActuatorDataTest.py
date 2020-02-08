import unittest

from labs.common import ActuatorData

class ActuatorDataTest(unittest.TestCase):
	"""
	Unittests for actuatorDataTest
	"""
	def setUp(self):
		'''
		Setting up resources
		'''
		self.actuatorTest = ActuatorData.ActuatorData()
		self.actuatorTest.command = "TestCommand"
		self.actuatorTest.value = 56251
		self.actuatorTest.name = "TestName"
		pass

	"""
	Tearing the resources down.
	"""
	def tearDown(self):
		self.actuatorTest = None
		pass
	
	"""
	Testing Retrieval of the actuator command from the actuatorData
	"""
	def testGetCommand(self):
		#Should return the command set in setUp
		self.assertEqual("TestCommand",self.actuatorTest.getCommand())
		pass

	
	"""
	Testing Retrieval of the actuator's name from the actuatorData
	"""
	def testGetName(self):
		#Should return the name set in setUp
		self.assertEqual("TestName",self.actuatorTest.getName())
		pass

	"""
	Testing Retrieval of the actuator's name from the actuatorData
	"""
	def testGetValue(self):
		#Should return the value set in setUp
		self.assertEqual(56251,self.actuatorTest.getValue())
		pass
	
	"""
	Testing if the setCommand method works as intended 
	"""
	def testSetCommand(self):
		#Testing if setCommand returns true for setting the data
		self.assertEqual(True,self.actuatorTest.setCommand("test"))
		#Testing if command was set properly
		self.assertEqual("test",self.actuatorTest.getCommand())
		pass
	
	"""
	Testing if the setName method works as intended 
	"""
	def testSetName(self):
		#Testing if setName returns true for setting the name
		self.assertEqual(True,self.actuatorTest.setName("test"))
		#Testing if name was set properly
		self.assertEqual("test",self.actuatorTest.getName())
		pass

	"""
	Testing if the setValue method works as intended 
	"""
	def testSetValue(self):
		#Testing if setName returns true for setting the name
		self.assertEqual(True,self.actuatorTest.setValue(7070))
		#Testing if name was set properly
		self.assertEqual(7070,self.actuatorTest.getValue())
		pass

	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()