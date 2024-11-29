from abc import ABC, abstractmethod

class GUIFactory(ABC):
    "An abstract factory interface used by the concrete factories."

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass