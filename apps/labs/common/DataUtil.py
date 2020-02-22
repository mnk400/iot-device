'''
Created on Feb 21, 2020

@author: manik
'''
import SensorData, ActuatorData
import json
class DataUtil(object):
    '''
    Class to handle JSON data,
    convert from JSON to sensorData or actuatorData instance
    or convert sensorData or actuatorDat instance to JSON.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def toSensorDataFromJson(self, jsonStr) -> SensorData.SensorData:
        '''
        Convert from JSON to SensorData instance
        '''
        #Loading the jsonString
        jsonData                = json.loads(jsonStr)
        #Creating a sensorData instance
        sensorData              = SensorData.SensorData()
        #Adding values to the sensorData Instance
        sensorData.currentValue = jsonData['currentValue']
        sensorData.totalCount   = jsonData['totalCount']
        sensorData.totalValue   = jsonData['totalValue']
        sensorData.maxValue     = jsonData['maxValue']
        sensorData.minValue     = jsonData['minValue']
        sensorData.timestamp    = jsonData['timestamp']
        sensorData.name         = jsonData['name']
        
        return sensorData

    def toJsonFromSensorData(self, sensorData: SensorData.SensorData) -> str:
        '''
        Convert from SensorData instance to JSON
        '''
        #Converting the sensorData to a dictionary
        jsonData = { 
                        "currentValue"  : sensorData.getCurrentValue(),
                        "totalCount"    : sensorData.getCount(),
                        "totalValue"    : sensorData.totalValue,
                        "maxValue"      : sensorData.getMinValue(),
                        "minValue"      : sensorData.getMaxValue(),
                        "timestamp"     : sensorData.timestamp,
                        "name"          : sensorData.getName()
        }
        #dumping the json data and returning it
        jsonStr = json.dumps(jsonData)
        return jsonStr
    
    def writeSensorDataToFile(self):
        '''
        Converts SensorData to JSON and writes to the filesystem
        '''
        pass

    def toActuatorDataFromJson(self, jsonStr) -> ActuatorData.ActuatorData:
        '''
        Convert from JSON to ActuatorData instance
        '''
        #Loading the jsonString
        jsonData                = json.loads(jsonStr)
        #Creating a sensorData instance
        actuatorData            = ActuatorData.ActuatorData()
        #Adding values to the sensorData Instance
        actuatorData.command    = jsonData['command']
        actuatorData.name       = jsonData['name']
        actuatorData.value      = jsonData['value']    
        return actuatorData

    def toJsonFromActuatorData(self,actuatorData: ActuatorData.ActuatorData) -> str:
        '''
        Convert from ActuatorData instance to JSON
        '''
        #Converting the actuatorData to a dictionary
        jsonData = { 
                        "command"   : actuatorData.getCommand(),
                        "name"      : actuatorData.getName(),
                        "value"     : actuatorData.getValue()
                        

        }
        #dumping the json data and returning it
        jsonStr = json.dumps(jsonData)
        return jsonStr  
    
    def writeActuatorDataToFile(self):
        '''
        Converts ActuatorData to JSON and writes to the filesystem
        '''
        pass

if __name__ == "__main__":
    
    s = SensorData.SensorData()
    s.addValue(10)
    obj = DataUtil()
    str1 = obj.toJsonFromSensorData(s)
    print(str1)
    m = obj.toSensorDataFromJson(str1)
    print("~~~~~~~~~~~~~~~~~~~")
    a = ActuatorData.ActuatorData()
    a.setCommand("TEST")
    a.setName("LOLOLOL")
    a.setValue(696969)
    str2 = obj.toJsonFromActuatorData(a)
    print(str2)
    k = obj.toActuatorDataFromJson(str2)
    print(k.getCommand())
    print(k.getValue())
    
