from project.lib.DeviceDataManager import DeviceDataManager

if __name__ == "__main__":
    '''
    Main method to execute the program
    '''
    projectApp = DeviceDataManager(4)           #Setting the sleep timer
    projectApp.checksBypass = False             #Not bypassing the sensorCheck
    projectApp.startupSequence()                #Executing startup sequence