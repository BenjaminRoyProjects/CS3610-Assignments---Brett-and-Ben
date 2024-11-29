from builder import Builder
from typing import Type
from Manual import Manual

class ManualBuilder(Builder):
    "Concrete builder class for Manuals."

    def __init__(self):
        self.reset()

    @property
    def Manual(self) -> Manual:
        return self.__Manual

    @Manual.setter
    def Manual(self, newManual: Type[Manual]) -> None:
        self.__Manual = newManual

    def reset(self) -> None:
        self.__Manual = Manual()

    def setSeats(self, number) -> None:
        self.__Manual.add(f'{number} seats')

    def setEngine(self, engine) -> None:
        self.__Manual.add(f'{engine} engine')

    def setTripComputer(self, number) -> None:
        self.__Manual.add(number)

    def setGPS(self, number) -> None:
        self.__Manual.add(number)

    def getResult(self) -> Manual:
        return self.Manual()
