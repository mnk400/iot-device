import unittest

from labs.module02 import SmtpClientConnector, TempEmulatorAdapter, TempSensorEmulatorTask
from labs.common import ConfigUtil, SensorData
class Module02Test(unittest.TestCase):

	def setUp(self):
		self.SmtpTest = SmtpClientConnector.MyClass()
		self.EmulatorTest = TempSensorEmulatorTask.TempSensorEmulator()
		pass

	def tearDown(self):
		pass

	def testPublishMessage(self):
		print("\n")
		if self.SmtpTest.config.configFileLoaded == True:
			print("Case 1 (Email should be sent): ", end = " ")
			self.assertEqual(True,self.SmtpTest.publishMessage("TestMail","Test Message"),"Failed")	
			print("Case 2 (SMTP should not connect): ", end = " ")
			self.SmtpTest.config.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")	
			self.SmtpTest.config.loadConfigData()
			self.assertEqual(False,self.SmtpTest.publishMessage("TestMail", "Test Message"),"Failed")
		else:
			self.SmtpTest.config.__init__("sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props")	
			self.SmtpTest.config.loadConfigData()
			print("Case Pipeline : ", end = " ")
			self.assertEqual.__init__(False,self.SmtpTest.publishMessage("TestMail", "Test Message"))
		pass

	def testGenerateData(self):
		print("\n")
		self.assertEqual(True,self.EmulatorTest.generateData())
		pass

	def testGetSensorData(self):
		print("\n")
		self.assertEqual(type(self.EmulatorTest.getSensorData()),SensorData.SensorData,)
		pass

	def testGenerateString(self):
		self.EmulatorTest.generateData()
		self.assertEqual(type(self.EmulatorTest.generateString()),str)
		pass

	def testRun_Emulation(self):
		Emulation = TempEmulatorAdapter.TempEmulatorAdapter()
		Emulation.enableTempEmulatorAdapter = True
		self.assertEqual(True,Emulation.run_emulation())
		Emulation.enableTempEmulatorAdapter = False
		self.assertEqual(False,Emulation.run_emulation())

		Emulation = TempEmulatorAdapter.TempEmulatorAdapter(1,0)
		Emulation.enableTempEmulatorAdapter = True
		self.assertEqual(True,Emulation.run_emulation())

		Emulation = TempEmulatorAdapter.TempEmulatorAdapter(-1,0)
		self.assertEqual(False,Emulation.run_emulation())

		Emulation = TempEmulatorAdapter.TempEmulatorAdapter(2,-1)
		self.assertEqual(False,Emulation.run_emulation())
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()