import unittest
import logging

from labs.module02 import SmtpClientConnector, TempEmulatorAdapter, TempSensorEmulatorTask
from labs.common import ConfigUtil, SensorData
class Module02Test(unittest.TestCase):
	'''
	Test class for classes in Module02 functionality.
	'''
	def setUp(self):
		#Get a SMTPclient instance
		self.SmtpTest 	  = SmtpClientConnector.MyClass()
		#Get a TempSensorEmulator instance
		self.EmulatorTest = TempSensorEmulatorTask.TempSensorEmulator()
		#Get a TempEmulatorAdapter instance
		self.Emulation    = TempEmulatorAdapter.TempEmulatorAdapter()
		pass

	def tearDown(self):
		self.SmtpTest     = None
		self.EmulatorTest = None
		self.Emulation    = None
		pass
	'''
	Testing the publicMessage method from SMTPClientConnector to check if emails 
	can be sent properly and if errors are handled properly
	'''	
	def testPublishMessage(self):
		print("\n")
		if self.SmtpTest.config.configFileLoaded == True:
			#If true the code will run locally where the real ConfigFile 
			logging.info("Case 1 (Email should be sent): ")
			#Case one where connection will establish and email will be sent
			self.assertEqual(True,self.SmtpTest.publishMessage("TestMail","Test Message"))	
			#Case two where connection will fail because of wrong data 
			#and the email will not be sent but method will return a false
			logging.info("Case 2 (SMTP should not connect): ")
			#loading wrong data intentionally 
			self.SmtpTest.config.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")	
			self.SmtpTest.config.loadConfigData()
			self.assertEqual(False,self.SmtpTest.publishMessage("TestMail", "Test Message"),"Failed")
		else:
			#If false the code will on the pipeline where the real ConfigFile doesn't exist
			#Load the Sample config file
			#Only case for the pipeline where the Sample config is loaded
			self.SmtpTest.config.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")	
			self.SmtpTest.config.loadConfigData()
			print("Case Pipeline : ", end = " ")
			#should return a false because the pipeline doesn't have correct config data
			self.assertEqual(False,self.SmtpTest.publishMessage("TestMail", "Test Message"))
		pass

	'''
	Testing GenerateData from TempEmulatorTask to generate new random data which is then stored in configUtil
	'''	
	def testGenerateData(self):
		print("\n")
		#generateData returns a true if the method ran as it was intended to
		#which it should 100% of the time
		#test failing would mean imply a bug in the code
		self.assertEqual(True,self.EmulatorTest.generateData())
		pass

	
	def testSendNotification(self):
		if(self.EmulatorTest.SmtpClient.config.configFileLoaded == True):
			self.assertEqual(True,self.EmulatorTest.sendNotification("send notif"))
		pass
	'''
	Testing SensorData from SensorDataTest to check if sensorData object is being returned
	'''	
	def testGetSensorData(self):
		print("\n")
		#Testing if getSensorData returns an object of the sensorData
		self.assertEqual(type(self.EmulatorTest.getSensorData()),SensorData.SensorData,)
		pass

	'''
	Testing the generate String method from TempEmulatorTask if method returns a String
	'''	
	def testGenerateString(self):
		self.EmulatorTest.generateData()
		#Testing if generateString method returns a String object
		self.assertEqual(type(self.EmulatorTest.generateString()),str)
		pass

	'''
	Testing the Run_Emulation from the TempEmulatorAdapter to check if the Emulation runs properly
	'''	
	def testRun_Emulation(self):
		#Running emulation when enable is true, we should be returned a true
		self.Emulation.enableTempEmulatorAdapter = True
		self.assertEqual(True,self.Emulation.run_emulation())
		#Running emulation when enable is false, we should be returned a false
		self.Emulation.enableTempEmulatorAdapter = False
		self.assertEqual(False,self.Emulation.run_emulation())

		#setting the looptime and sleeptime to 1 and 0, should run once and return a true
		self.Emulation.__init__(1,0)
		self.Emulation.enableTempEmulatorAdapter = True
		self.assertEqual(True,self.Emulation.run_emulation())
		
		#setting the looptime and sleeptime to -1 and 0, should not run and return a false
		self.Emulation.__init__(-1,0)
		self.assertEqual(False,self.Emulation.run_emulation())

		#setting the looptime and sleeptime to 2 and -2, should not run and return a false
		self.Emulation.__init__(2,-1)
		self.assertEqual(False,self.Emulation.run_emulation())
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()