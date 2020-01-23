import unittest
"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
import threading
from labs.module01 import SystemCpuUtilTask, SystemMemUtilTask, SystemPerformanceAdapter
class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.cpu_test = SystemCpuUtilTask.Cpu()
		self.mem_test = SystemMemUtilTask.Mem()
		self.adaptor_test = SystemPerformanceAdapter.SystemPerformanceAdapter(2,5) 
		self.adaptor_test.daemon = True
		self.atest_thread = threading.Thread(target=self.adaptor_test.run_adapter())

		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	Place your comments describing the test here.
	"""
	def testSystemCpuUtilTask(self):
		cpuPer = self.cpu_test.getDataFromSensor()
		
		self.assertGreater(100,cpuPer,"CPU over 100")
		self.assertLessEqual(0,cpuPer, "CPU less than or equal to 100")

	def testSystemMemUtilTask(self):
		memPer = self.mem_test.getDataFromSensor()
		
		self.assertGreater(100,memPer,"Memory over 100")
		self.assertLessEqual(0,memPer, "Memory less than or equal to 100")
		
	def testSystemPerformanceAdapter(self):	
		self.atest_thread.start()
		pass	
			

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()