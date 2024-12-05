#ForecastSensors
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

import random

class ForecastSensors():
    NUMREADINGS = 5 #Number of readings to "receive from the sensors"
    TEMPDEVIATION = 5 #Deviation of "sensor data"
    
    def getForecastData(self):
        #Generate a list of temperatures "from the sensors". Returned as a binary list.
        avgTempList = []
        randtemp = random.randrange(-40, 40) #Random temp that the others will be based on
        for day in range(self.NUMREADINGS):
            #Generate a temperature for each day based on the random temperature generated prior
            avgTempList.append(random.randrange((randtemp - self.TEMPDEVIATION), (randtemp + self.TEMPDEVIATION)))
        #Convert forecast data to binary
        binaryTemps = []
        for temp in avgTempList:
            binaryTemps.append(str(temp).encode("utf-8"))
        return binaryTemps