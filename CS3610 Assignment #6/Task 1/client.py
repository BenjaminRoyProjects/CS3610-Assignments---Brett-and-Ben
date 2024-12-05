#Client
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from ForecastSensors import ForecastSensors
from ForecastSystem import ForecastSystem
from Adapter import Adapter
from ClientInterface import ClientInterface

class Client(ClientInterface):
  
  def forecast(self, service):
    return service.getForecastData()
  
    serv1 = ForecastSystem()
    adapter1 = Adapter(serv1)
    bindata = adapter1.getForecastData()
    print(bindata)


#cd CS3610\ Assignment\ #6/Task\ 1
#python client.py