#Button
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from abc import ABC, abstractmethod

class Button(ABC):
    #Abstract product class.

    @property
    @abstractmethod
    def statement(self) -> None:
        #Getter for statement.
        pass

    @abstractmethod
    def press(self) -> None:
        #Presses the button.
        pass