from abc import ABC, abstractmethod

class Checkbox(ABC):
    "Abstract product class."

    @property
    @abstractmethod
    def isChecked(self) -> bool:
        "Getter for isChecked."
        pass

    @abstractmethod
    def check(self) -> None:
        "Checks the checkbox."
        pass