#GUIFactory
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from abc import ABC, abstractmethod
from Button import Button
from Checkbox import Checkbox

class GUIFactory(ABC):
    #An abstract factory interface used by the concrete factories.

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass