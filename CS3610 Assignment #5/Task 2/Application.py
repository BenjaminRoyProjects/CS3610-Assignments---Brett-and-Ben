from GUIFactory import GUIFactory
from MacFactory import MacFactory
from WinFactory import WinFactory
from typing import Type

class Application:
    "Client application."

    def __init__(self, factory: Type[GUIFactory]):
        self.__factory = factory

    @property
    def factory(self) -> GUIFactory:
        return self.__factory

    @factory.setter
    def factory(self, factory: GUIFactory) -> None:
        self.__factory = factory

    @property
    def button(self) -> Button:
        return self.__button

    @button.setter
    def button(self, button: Button) -> None:
        self.__button = button

    def createUI(self):
        "Creates "
        


    def paint(self):
        pass
