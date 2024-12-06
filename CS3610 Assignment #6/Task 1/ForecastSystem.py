#ForecastSystem
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from typing import Type
import xml.etree.ElementTree as ElTree

class ForecastSystem():
  def cleanXMLData(self, data: Type[str]):
    #Display input data
    print("Forecast System has received input data:")
    print(data)
    #Convert the xml string back into an element tree
    xmltree = ElTree.fromstring(data)
    #Extract the reading data from the element tree
    readings = xmltree.findall(".//temp")
    #Find the average of the temperatures
    average = 0
    for reading in readings:
      average += int(reading.text)
    average = average / len(readings)
    #Form a string of temperature readings averaged with the overall average of the readings reading
    listtemps = []
    for reading in readings:
      #Average the reading with the overall average, rounded to one decimal place
      accreading = (int(reading.text) + average)/2
      accreading = round(accreading, 1)
      listtemps.append(accreading)
    return listtemps
