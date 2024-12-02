from GUIFactory import GUIFactory
from MacFactory import MacFactory
from WinFactory import WinFactory
from typing import Type

class Application:
    "Client application."

    def __init__(self, factory: Type[GUIFactory]):
        self.__factory = factory
        self.__elements = []

    @property
    def factory(self) -> GUIFactory:
        return self.__factory

    @factory.setter
    def factory(self, factory: GUIFactory) -> None:
        self.__factory = factory

    def createUI(self):
        "Creates and fills the Application's component field"
        self.__elements.append(self.__factory.createButton())
        self.__elements.append(self.__factory.createButton())
        self.__elements.append(self.__factory.createCheckbox())
        self.__elements.append(self.__factory.createButton())


    def paint(self):
        print("Elements: ", end="")
        if len(self.__elements) > 0:
            for element in self.__elements:
                print(f"{element} ", end="")
            print("")
        else:
            print("None")