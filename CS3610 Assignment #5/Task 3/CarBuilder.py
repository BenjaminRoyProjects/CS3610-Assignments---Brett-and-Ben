from builder import Builder
from typing import Type
from car import Car

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
        self.__car.add(f'{number} seats')

    def setEngine(self, engine) -> None:
        self.__car.add(f'{engine} engine')

    def setTripComputer(self) -> None:
        self.__car.add('Standard Trip')

    def setGPS(self) -> None:
        self.__car.add('Standard GPS')

    def getResult(self) -> Car:
        return self.car()
