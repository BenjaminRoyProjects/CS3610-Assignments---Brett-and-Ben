from abc import ABC, abstractmethod

class Button(ABC):
    "Abstract product class."

    @property
    @abstractmethod
    def statement(self) -> None:
        "Getter for statement."
        pass

    @abstractmethod
    def press(self) -> None:
        "Presses the button."
        pass