import unittest
from project.lib.CoAPClientConnector import CoAPClientConnector
from project.lib.SenseHatUpdater import SenseHatUpdater
from project.lib.DeviceDataManager import DeviceDataManager
from project.lib.HeartRateTask import HeartRateTask
from project.lib.SpO2Task import SpO2Task
from project.lib.SystemCpuUtilTask import Cpu
from project.lib.SystemMemUtilTask import Mem
from project.lib.MqttClientConnector import MqttClientConnector
from project.lib.SerialCommunicator import SerialCommunicator
from labs.common import SensorData, ActuatorData
import asyncio
from time import sleep

class ProjectTest(unittest.TestCase):

	"""
	Setting up resources 
	"""
	def setUp(self):
		#CoAPClient
		self.coAPTest = CoAPClientConnector()

		#SenseHatUpdater 
		self.senseHatUpdater = SenseHatUpdater()

		#Mqtt
		self.mqttTest = MqttClientConnector()

		#DeviceDataManager
		self.manager = DeviceDataManager()

		#SerialCommunicator
		self.ser = SerialCommunicator(baud=152000,looplimit=1)

		#HeartRateTask
		self.hr = HeartRateTask(self.coAPTest, looplimit=1)

		#HeartRateTask
		self.spo = SpO2Task(self.coAPTest, looplimit=1)

		#CPUUtil Task
		self.cpu = Cpu(self.coAPTest, looplimit=1)

		#MemUtil Task
		self.mem = Mem(self.coAPTest, looplimit=1)

		#Getting an asyncio event loop
		self.loop = asyncio.get_event_loop()

		#SensorData object
		self.sensorData = SensorData.SensorData()
		self.sensorData.addValue(10)
		self.sensorData.setName("TESTNAME")

		#ActuatorData object
		self.actuatorData = ActuatorData.ActuatorData()
		self.actuatorData.setCommand("TESTCOMMAND")
		self.actuatorData.setValue("TESTVALUE")
		self.actuatorData.setName("TESTNAME")

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.coAPTest = None
		self.sensorData = None
		self.actuatorData = None
		self.senseHatUpdater = None
		self.loop = None
	
	'''
	Testing updateActuator in SenseHatUpdater
	'''
	def testUpdateActuator(self):

		#Should return false when command is wrong
		self.actuatorData.setCommand("wrongcommand")
		self.assertEqual(False,self.senseHatUpdater.updateActuator(self.actuatorData))

	'''
	Testing the clear function in senseHatUpdater
	'''
	def testClear(self):
		#Should always return true
		self.assertEqual(True,self.senseHatUpdater.clear())

	'''
	Testing serialRead in serialcommunicator
	'''
	def testSerialRead(self):
		#should always return true
		self.assertEqual(True,self.ser.serialRead())
	
	'''
	Testing serialWrite in serialcommunicator
	'''
	def testSerialWrite(self):
		#should always return true
		self.assertEqual(True,self.ser.serialWrite("string"))

	'''
	Testing StartupSequence in DeviceDataManager
	'''
	def testStartupSequence(self):
		#Should always return true
		self.manager.enableSerial = False
		self.manager.enableAdapter = False
		self.manager.enableTasks = False
		self.assertEqual(True,self.manager.startupSequence())

	'''
	Testing the run method in HeartRateTask
	'''
	def testHRRun(self):
		#Should always return true
		self.assertEqual(True, self.hr.run())

	'''
	Testing the run method in Spo2Task
	'''
	def testSpoRun(self):
		#Should always return true
		self.assertEqual(True, self.spo.run())
	
	'''
	Testing the run method in CpuTask
	'''
	def testCpuRun(self):
		#Should always return true
		self.assertEqual(True, self.cpu.run())
	
	'''
	Testing the run method in MemTask
	'''
	def testMemRun(self):
		#Should always return true
		self.assertEqual(True, self.mem.run())
	
	'''
	Testing dataPUT in CoAPClientConnector
	'''	
	def testDataPUT(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataPUT("TEST STRING")))

	'''
	Testing dataPOST in CoAPClientConnector
	'''	
	def testDataPOST(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataPOST("TEST STRING")))
	
	'''
	Testing dataGET in CoAPClientConnector
	'''	
	def testDataGET(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataGET()))

	'''
	Testing dataDelete in CoAPClientConnector
	'''	
	def testDataDelete(self):
		#Should always return true no matter if the message could be
		#sent or not, errors are in the logs
		self.assertEqual(True,self.loop.run_until_complete(self.coAPTest.dataDelete()))

	'''
	Testing getData in CoAPClientConnector
	'''
	def testGetData(self):
		#Should always return a True
		self.assertEqual(True,self.coAPTest.getData(self.loop))
	
	'''
	Testing deleteData in CoAPClientConnector
	'''
	def testDeleteData(self):
		#Should always return a True
		self.assertEqual(True,self.coAPTest.deleteData(self.loop))

	'''
	Testing sendSensorDataPUT in CoAPClientConnector
	'''
	def testSendSensorDataPUT(self):
		#Should return false when input not SensorData
		self.assertEqual(False,self.coAPTest.sendSensorDataPUT(self.loop,object))
		#Should return true when input is SensorData
		self.assertEqual(True,self.coAPTest.sendSensorDataPUT(self.loop,self.sensorData))
	
	'''
	Testing sendSensorDataPOST in CoAPClientConnector
	'''
	def testSendSensorDataPOST(self):
		#Should return false when input not SensorData
		self.assertEqual(False,self.coAPTest.sendSensorDataPOST(self.loop,object))
		#Should return true when input is SensorData
		self.assertEqual(True,self.coAPTest.sendSensorDataPOST(self.loop,self.sensorData))
	'''
	Testing PublishActuatorData in MqttClientConnector
	'''	
	def testPublishActuatorData(self):
		#Testing case when wrong input
		tempObj = object()
		self.assertEqual(False,self.mqttTest.publishActuatorData(tempObj))
		#Testing when the connected is False
		self.assertEqual(False,self.mqttTest.publishActuatorData(self.actuatorData))
		#Testing when connected, not running this in the pipeline, should return true
		self.mqttTest.connectActuatorData()
		self.assertEqual(False,self.mqttTest.publishActuatorData(self.actuatorData))
		

	'''
	Testing PublishSensorData in MqttClientConnector
	'''	
	def testPublishSensorData(self):
		#Testing case when wrong input
		tempObj = object()
		self.assertEqual(False,self.mqttTest.publishSensorData(tempObj))
		#Testing when the connected is False
		self.assertEqual(False,self.mqttTest.publishSensorData(self.sensorData))
		#Testing when connected, not running this in the pipeline, should return a True
		self.mqttTest.connectSensorData()
		self.assertEqual(False,self.mqttTest.publishSensorData(self.sensorData))
	
	'''
	Testing PublishOther in MqttClientConnector
	'''	
	def testPublishOther(self):
		#Testing when the connected is False
		self.assertEqual(False,self.mqttTest.publishSensorData("tempString"))
		#Testing when connected, not running this in the pipeline, should return a True
		self.mqttTest.connectSensorData()
		self.assertEqual(False,self.mqttTest.publishSensorData("tempString"))

	'''
	Testing ConnectActuatorData in MqttClientConnector
	'''	
	def testConnectActuatorData(self):
		#Should always return true
		self.assertEqual(True,self.mqttTest.connectActuatorData())

	'''
	Testing ConnectSensorData in MqttClientConnector
	'''	
	def testConnectSensorData(self):
		#Should always return true
		self.assertEqual(True,self.mqttTest.connectSensorData())


	'''
	Testing ListenActuatorData in MqttClientConnector
	'''	
	def testListenActuatorData(self):
		#Should return a false when not connected
		self.assertEqual(False,self.mqttTest.listenActuatorData())
		#Should return a true when connected
		self.mqttTest.connectActuatorData()
		sleep(1)
		self.assertEqual(True,self.mqttTest.listenActuatorData())
		self.mqttTest.disconnect()		

	'''
	Testing ListenSensorData in MqttClientConnector
	'''	
	def testListenSensorData(self):
		#Should return a false when not connected
		self.assertEqual(False,self.mqttTest.listenSensorData())
		#Should return a true when connected
		self.mqttTest.connectSensorData()
		sleep(1)
		self.assertEqual(True,self.mqttTest.listenSensorData())
		self.mqttTest.disconnect()
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()