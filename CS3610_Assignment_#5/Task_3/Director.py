#Director
#CS3610 Assignment #5
#Brett and Ben
#Dec 6, 2024

from typing import Type
from Builder import Builder

class Director:
    "Class usable by client code to automatically control builders."

    def __init__(self, builder: Type[Builder]):
        self.__builder = builder

    @property
    def builder(self) -> Builder:
        return self.__builder

    @builder.setter
    def builder(self, newbuilder: Type[Builder]) -> None:
        self.__builder = newbuilder

    def makeSUV(self) -> None:
        self.__builder.reset()
        self.__builder.setSeats("4")
        self.__builder.setEngine("SUVEngine")
        self.__builder.setTripComputer()
        self.__builder.setGPS()

    def makeSportsCar(self) -> None:
        self.__builder.reset()
        self.__builder.setSeats("2")
        self.__builder.setEngine("SportEngine")
        self.__builder.setTripComputer()
        self.__builder.setGPS()
