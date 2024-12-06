#Checkbox
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from abc import ABC, abstractmethod

class Checkbox(ABC):
    #Abstract product class.

    @property
    @abstractmethod
    def isChecked(self) -> bool:
        #Getter for isChecked.
        pass

    @abstractmethod
    def check(self) -> None:
        #Checks the checkbox.
        pass