#Adapter
#CS3610 Assignment #6
#Brett and Ben
#Dec 6, 2024

from ForecastSensors import ForecastSensors
from ForecastSystem import ForecastSystem
from typing import Type
import xml.etree.ElementTree as ElTree

class Adapter(ForecastSensors):
    def __init__(self, service: Type[ForecastSystem]):
        self.__adaptee = service #Instance of ForecastSystem class

    #Convert binary temperature data to xml format
    def binToXML(self, data: Type[bytes])
        strData = []
        for entry in data:
            strData.append(entry.decode("utf-8"))
        #Convert the list of strings into an XML tree
        tempdata = ElTree.Element("tempdata")
        tempdatadict = {}
        i = 0
        for tempreading in strData:
            tempdatadict[i] = ElTree.SubElement(tempdata, f"Reading {i}")
            tempdatadict[i].text = tempreading
            i += 1
        return ElTree.tostring(tempdata, "unicode")
        
    #Get data from the forecast sensors, convert it, and pass it to the forecast system
    def getForecastData(self):
        #Use ForecastSensors method to fetch data
        binData = super().getForecastData()
        xmlData = self.binToXML(binData)
        #Pass the XML data to the ForecastSystem
        self.__adaptee.cleanXMLData(xmlData)
        
        
        #Return the XML formatted data
        return 
        
    