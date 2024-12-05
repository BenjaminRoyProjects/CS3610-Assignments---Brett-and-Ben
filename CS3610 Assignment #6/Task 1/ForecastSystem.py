#ForecastSystem
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from typing import Type
import xml.etree.ElementTree as ElTree

class ForecastSystem():
  def cleanXMLData(self, data: Type[xml]):
    tempdata = ElTree.fromstring(data)
    print(tempdata)
    