import unittest

import threading
from labs.module01 import SystemCpuUtilTask, SystemMemUtilTask, SystemPerformanceAdapter
class Module01Test(unittest.TestCase):

	def setUp(self):
		self.cpu_test = SystemCpuUtilTask.Cpu()
		self.mem_test = SystemMemUtilTask.Mem()
		self.adaptor_test = SystemPerformanceAdapter.SystemPerformanceAdapter(1,1) 
		self.adaptor_test.daemon = True
		self.adaptor_test.enableSystemPerformanceAdapter = False
		self.testThread = threading.Thread(target=self.adaptor_test.run_adapter())

		pass

	def tearDown(self):
		pass
	
	'''
	Testing the return method from SystemCpuUtilTask
	'''
	def testSystemCpuUtilTask(self):
		cpuPer = self.cpu_test.getDataFromSensor()
		
		self.assertGreater(100,cpuPer,"CPU over 100")
		self.assertLessEqual(0,cpuPer, "CPU less than or equal to 100")

	'''
	Testing the return method from SystemMemUtilTask
	'''
	def testSystemMemUtilTask(self):
		memPer = self.mem_test.getDataFromSensor()
		
		self.assertGreater(100,memPer,"Memory over 100")
		self.assertLessEqual(0,memPer, "Memory less than or equal to 100")
	
	'''
	Testing the run_adapter from SystemPerformanceAdapter 
	'''	
	def testSystemPerformanceAdapter(self):
		print("\n")
		self.assertEqual(self.adaptor_test.run_adapter(), False, "True when expected False")
		self.adaptor_test.enableSystemPerformanceAdapter = True
		self.assertEqual(self.adaptor_test.run_adapter(), True, "False when expected True")
			

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()