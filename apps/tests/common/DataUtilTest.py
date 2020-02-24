import unittest
from labs.common import DataUtil, ActuatorData, SensorData

class DataUtilTest(unittest.TestCase):

	"""
	Setting up resources
	"""
	def setUp(self):
		#JSON strings to test on
		self.sensorJSON = "{\"currentValue\": 10.0, \"totalCount\": 1, \"totalValue\": 10.0, \"maxValue\": 10.0, \"minValue\": 10.0, \"timestamp\": \"2020-02-23 16:29:41.32\", \"name\": \"Temperature\"}"
		self.actuatorJSON = "{\"command\": \"Decrease\", \"name\": \"Temperature Sensor Data\", \"value\": \"DOWNARROW\"}"
		#ActuatorData instance filled with data
		self.actuatorData = ActuatorData.ActuatorData()
		self.actuatorData.setName("TestActuator")
		self.actuatorData.setCommand("TestCommand")
		self.actuatorData.setValue(0.0)
		#SensorData instance filled with data
		self.sensorData = SensorData.SensorData()
		self.sensorData.setName("TestSensor")
		self.sensorData.addValue(10)
		#Datautil Instance
		self.dataUtil = DataUtil.DataUtil()
		
		pass

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.actuatorData = None
		self.sensorData = None
		pass
	
	
	def testToJsonFromActuatorData(self):
		'''
		Testing if ActuatorData instance is converted to JSON properly.
		'''
		#Reading the json from the method
		jsonStr = self.dataUtil.toJsonFromActuatorData(self.actuatorData)
		#Converting the json to actuatorData instace to check if both the instances are the same
		tempActuatorData = self.dataUtil.toActuatorDataFromJson(jsonStr)
		#Following datapoints in the instance should be equal
		self.assertEqual(self.actuatorData.getValue(), tempActuatorData.getValue())
		self.assertEqual(self.actuatorData.getName(), tempActuatorData.getName())
		self.assertEqual(self.actuatorData.getCommand(), tempActuatorData.getCommand())
	
	
	def testToActuatorDataFromJson(self):	
		'''
		Testing if JSON strings are created properly from ActuatorData
		'''
		#Creating an actuatroData instance
		tempActuatorData = self.dataUtil.toActuatorDataFromJson(self.actuatorJSON)
		#Creaing a json string usinf the above instance
		jsonStr = self.dataUtil.toJsonFromActuatorData(tempActuatorData)
		self.assertEqual(self.actuatorJSON, jsonStr)
	
	
	def testToJsonFromSensorData(self):
		'''
		Testing if SensorData instance is converted to JSON properly
		'''
		#Reading the json from the method
		jsonStr = self.dataUtil.toJsonFromSensorData(self.sensorData)
		#Converting the json to actuatorData instace to check if both the instances are the same
		tempSensorData = self.dataUtil.toSensorDataFromJson(jsonStr)
		#Following datapoints in the instance should be equal
		self.assertEqual(self.sensorData.getName(), tempSensorData.getName())
		self.assertEqual(self.sensorData.getAverageValue(), tempSensorData.getAverageValue())
		self.assertEqual(self.sensorData.getCurrentValue(), tempSensorData.getCurrentValue())
		self.assertEqual(self.sensorData.getMaxValue(), tempSensorData.getMaxValue())
		self.assertEqual(self.sensorData.getMinValue(), tempSensorData.getMinValue())
		self.assertEqual(self.sensorData.totalCount, tempSensorData.totalCount)	
	
	
	def testToSensorDataFromJson(self):
		'''
		Testing if JSON strings are created properly from sensorData
		'''
		#Creating an actuatroData instance
		tempSensorData = self.dataUtil.toSensorDataFromJson(self.sensorJSON)
		#Creaing a json string usinf the above instance
		jsonStr = self.dataUtil.toJsonFromSensorData(tempSensorData)
		self.assertEqual(self.sensorJSON, jsonStr)
	
	
	
	def testWriteActuatorDataToFile(self):
		'''
		Testing if data is being written to log file
		'''	
		#Checking if we can write an object of actuatorData to the lof file.
		self.assertEqual(True, self.dataUtil.writeActuatorDataToFile(self.dataUtil.toJsonFromActuatorData(self.actuatorData)))
	
	
	def testWriteSensorDataToFile(self):
		'''
		Testing if data is being written to log file
		'''
		#Checking if we can write an object of sensorData to the lof file.
		self.assertEqual(True, self.dataUtil.writeSensorDataToFile(self.dataUtil.toJsonFromSensorData(self.sensorData)))
	
if __name__ == "__main__":
	#import syssys.argv = ['', 'Test.testName']
	unittest.main()