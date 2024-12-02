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

    def listElements(self) -> None:
        if len(self.__components) > 0:
            for element in self.__elements:
                print("Elements: ", end="")
                print(f"{element} ", end="")
            print("")

    def addButton(self, button: Button) -> None:
        print("Adding button to UI...")
        self.__elements.append(button)

    def addCheckbox(self, checkbox: Checkbox) -> None:
        print("Adding checkbox to UI...")
        self.__elements.append(checkbox)

    def createUI(self):
        "Creates and fills the Application's component field"
        self.addButton(self.__factory.createButton())


    def paint(self):
        pass
