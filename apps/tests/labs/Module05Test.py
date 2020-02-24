import unittest
from labs.module05 import MultiActuatorAdapter, MultiSensorAdapter, TempSensorAdapterTask
from labs.common import SensorData, ActuatorData, PersistenceUtil

class Module05Test(unittest.TestCase):

	"""
	Setting up resources 
	"""
	def setUp(self):
		#Setting up resources from common
		self.pUtil = PersistenceUtil.PersistenceUtil()
		self.multiActuatorAdapterTest = MultiActuatorAdapter.MultiActuatorAdapter()
		self.tempSensorAdapterTaskTest = TempSensorAdapterTask.TempSensorAdapterTask(1,1,self.pUtil)
		self.multiSensorAdapterTest = MultiSensorAdapter.MultiSensorAdapter(1,1)

	"""
	Getting rid of resources
	"""
	def tearDown(self):
		self.MultiActuatorAdapterTest = None
		self.tempSensorAdapterTaskTest = None
		self.multiSensorAdapterTest = None
	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testUpdateActuator(self):
		#Creating a temporary actuatorData instance
		actuator = ActuatorData.ActuatorData()
		actuator.setCommand("Print")
		actuator.setValue(["TEST",(90,200,90)])
		#Checking for a compatible command
		self.assertEqual(True,self.multiActuatorAdapterTest.updateActuator(actuator))
		#Checking for an incompatible command
		actuator.setCommand("This shouldn't work")
		self.assertEqual(False,self.multiActuatorAdapterTest.updateActuator(actuator))
		self.multiActuatorAdapterTest.clear()

	'''
	Testing the testUpdateActuator function in MultiActuatorAdapter
	'''
	def testClear(self):
		#Testing the clear function
		self.assertEqual(True,self.multiActuatorAdapterTest.clear())

	'''
	Testing the run function in TempSensorAdapterTask
	'''
	def testRun(self):
		#Should always return a True, no matter what the parameters
		self.assertEqual(True, self.tempSensorAdapterTaskTest.run())
		pass

	'''
	Testing the run function in TempSensorAdapterTask
	'''
	def test__init__threads__(self):
		#Testing the function which runs threads
		#Should not run when setting disabled and return False
		self.multiSensorAdapterTest.enableTempTask = False
		self.assertEqual(False,self.multiSensorAdapterTest.__init_threads__())
		self.multiSensorAdapterTest.enableTempTask = True
		#Should run when setting is enabled
		self.assertEqual(True,self.multiSensorAdapterTest.__init_threads__())
		pass

	'''
	Testing the testGenerateString function in TempSensorAdapterTask
	'''
	def testGenerateString(self):
		#Should return an object of type string
		self.tempSensorAdapterTaskTest.sensorData.addValue(20)
		self.assertEqual(str, type(self.tempSensorAdapterTaskTest.generateString()))
		pass
			
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()