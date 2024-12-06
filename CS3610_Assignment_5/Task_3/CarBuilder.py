#CarBuilder
#CS3610 Assignment #5
#Brett and Ben
#Dec 6, 2024

from Builder import Builder
from typing import Type
from Car import Car

class CarBuilder(Builder):
    "Concrete builder class for cars."

    def __init__(self):
        self.reset()

    @property
    def car(self) -> Car:
        return self.__car

    @car.setter
    def car(self, newcar: Type[Car]) -> None:
        self.__car = newcar

    def reset(self) -> None:
        self.__car = Car()

    def setSeats(self, number) -> None:
        self.__car.add(f'<{number} Seats>')

    def setEngine(self, engine) -> None:
        self.__car.add(f'<{engine} Engine>')

    def setTripComputer(self) -> None:
        self.__car.add('<Standard Trip>')

    def setGPS(self) -> None:
        self.__car.add('<Standard GPS>')

    def getResult(self) -> Car:
        return self.__car
