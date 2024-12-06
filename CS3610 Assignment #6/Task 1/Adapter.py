#Adapter
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from ForecastSensors import ForecastSensors
from ForecastSystem import ForecastSystem
from typing import Type
import xml.etree.ElementTree as ElTree

class Adapter(ForecastSensors):
    def __init__(self, forecastservice: Type[ForecastSystem]): 
        self.__fcsystem = forecastservice #Instance of ForecastSystem class

    #Convert binary temperature data to xml format
    def binToXML(self, data: Type[bytes]):
        strData = []
        for entry in data:
            strData.append(entry.decode("utf-8"))
        #Convert the list of strings into an XML tree
        tempdata = ElTree.Element("tempdata")
        tmp = None
        for tempreading in strData:
            tmp = ElTree.SubElement(tempdata, f"temp")
            tmp.text = tempreading
        return tempdata
        
    #Get data from the forecast sensors, convert it, and pass it to the forecast system
    def getForecastData(self):
        #Use ForecastSensors method to fetch data
        binData = super().getForecastData()
        #Convert the data from binary to an XML ElementTree to a string of XML data
        xmlData = self.binToXML(binData)
        strXMLData = ElTree.tostring(xmlData, encoding="unicode")
        #Pass the xml data to the new system and return its cleaner data
        return self.__fcsystem.cleanXMLData(strXMLData)
