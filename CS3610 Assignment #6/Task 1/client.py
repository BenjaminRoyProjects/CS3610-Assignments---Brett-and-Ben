#Client
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from ForecastSensors import ForecastSensors
from ForecastSystem import ForecastSystem
from Adapter import Adapter
from ClientInterface import ClientInterface
  
#
def forecast(self, service):
  return service.getForecastData()

#Main
serv1 = ForecastSystem()
print(forecast(serv1))


#cd CS3610\ Assignment\ #6/Task\ 1
#python client.py