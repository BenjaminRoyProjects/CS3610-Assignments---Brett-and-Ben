#ForecastSensors
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

import random

class ForecastSensors():
    __NUMREADINGS = 5 #Number of readings to "receive from the sensors"
    __TEMPDEVIATION = 5 #Deviation of "sensor data"
    __RANDOMTEMPRANGE = 20 #Temperatures generated will be between the + and - of this integer
    
    def getForecastData(self):
        #Generate a list of temperatures "from the sensors". Returned as a binary list.
        avgTempList = []
        randtemp = random.randrange(0 - self.__RANDOMTEMPRANGE, self.__RANDOMTEMPRANGE) #Random temp that the others will be based on
        for day in range(self.__NUMREADINGS):
            #Generate a temperature for each day based on the random temperature generated prior
            avgTempList.append(random.randrange((randtemp - self.__TEMPDEVIATION), (randtemp + self.__TEMPDEVIATION)))
        #Convert forecast data to a list of bytes and return it
        binaryTemps = []
        for temp in avgTempList:
            binaryTemps.append(str(temp).encode("utf-8"))
        return binaryTemps
