#Client
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from ForecastSensors import ForecastSensors
from ForecastSystem import ForecastSystem
from Adapter import Adapter
from typing import Type

class Client():
  #Take a forecastsensor object and collect sensor data from it
  def forecast(self, source: Type[ForecastSensors]):
    print("Running forecast system...")
    tempdata = source.getForecastData()
    print(f"Sensor forecast data: {tempdata}", end="\n\n")

#Main
app1 = Client()
sens1 = ForecastSensors()
print("Using old system:")
app1.forecast(sens1) #
serv1 = ForecastSystem()
adap1 = Adapter(serv1)
print("Using new system:")
app1.forecast(adap1)

#cd CS3610\ Assignment\ #6/Task\ 1
#python client.py
