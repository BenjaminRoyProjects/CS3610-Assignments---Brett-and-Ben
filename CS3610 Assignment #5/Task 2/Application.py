#Application
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from GUIFactory import GUIFactory
from MacFactory import MacFactory
from WinFactory import WinFactory
from typing import Type

class Application:
    #Client application.

    def __init__(self, factory: Type[GUIFactory]):
        self.__factory = factory
        self.__elements = []
        #self.__button = None
        #self.__checkbox = None

    @property
    def factory(self) -> GUIFactory:
        return self.__factory

    @factory.setter
    def factory(self, factory: GUIFactory) -> None:
        self.__factory = factory

    def createUI(self):
        #Fills the Application's UI field(s)
        self.__elements.append(self.__factory.createButton())
        self.__elements.append(self.__factory.createButton())
        self.__elements.append(self.__factory.createCheckbox())
        self.__elements.append(self.__factory.createButton())
        #self.__button = self.factory.createButton()
        #self.__checkbox = self.factory.createCheckbox()


    def paint(self):
        #Prints the contents of the Application's UI field(s)
        print("Elements: ", end="")
        if len(self.__elements) > 0:
            for element in self.__elements:
                print(f"{element} ", end="")
            print("")
        else:
            print("None")
        #print(f"Button: {self.__button}")
        #print(f"Checkbox: {self.__checkbox}")