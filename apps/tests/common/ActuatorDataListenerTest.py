import unittest
from labs.common import ActuatorData, ActuatorDataListener
from os import path
import redis
from time import sleep

class ActuatorUtilTest(unittest.TestCase):
    """
    Testing methods from ActuatorUtilTest Class
    """

    """
    Setting up resources
    """
    def setUp(self):
        rUtil = redis.Redis()
        #Creating a listener instance
        self.listener = ActuatorDataListener.ActuatorDataListener(rUtil)
        #ActuatorData instance filled with data
        self.actuatorData = ActuatorData.ActuatorData()
        self.actuatorData.setName("TestActuator")
        self.actuatorData.setCommand("Stable")
        self.actuatorData.setValue("TICK")
		

        
    """
    Getting rid of resources
    """
    def tearDown(self):
        self.actuatorData = None
        self.listener = None
        pass

    def testOnMessage(self):
        '''
        Testing if onMessage actuates the actuator as it should
        '''
        #Passing the actuatorData we defined instance in the method
        self.listener.onMessage(self.actuatorData)
        sleep(0.5)
        #Clearing actuator
        self.listener.actuatorAdapter.clear()
	
if __name__ == "__main__":
	#import syssys.argv = ['', 'Test.testName']
	unittest.main()