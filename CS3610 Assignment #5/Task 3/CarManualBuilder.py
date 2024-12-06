#CarManualBuilder
#CS3610 Assignment #5
#Brett and Ben
#Dec 6, 2024

from Builder import Builder
from typing import Type
from Manual import Manual

class ManualBuilder(Builder):
    "Concrete builder class for Manuals."

    def __init__(self):
        self.reset()

    @property
    def Manual(self) -> Manual:
        return self.__manual

    @Manual.setter
    def Manual(self, newManual: Type[Manual]) -> None:
        self.__manual = newManual

    def reset(self) -> None:
        self.__manual = Manual()

    def setSeats(self, number) -> None:
        self.__manual.add(f'<{number} Seats>')

    def setEngine(self, engine) -> None:
        self.__manual.add(f'<{engine} Engine>')

    def setTripComputer(self) -> None:
        self.__manual.add('<Standard Trip>')

    def setGPS(self) -> None:
        self.__manual.add('<Standard GPS>')

    def getResult(self) -> Manual:
        return self.__manual
