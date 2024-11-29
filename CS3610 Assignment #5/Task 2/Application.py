#from GUIFactory import GUIFactory
from typing import Type

class Application:
    "Client application."

    "Static dictionary of supported operating systems and their corresponding factories."
    supportedOSDict = {"WINDOWS": WinFactory, "MAC": MacFactory}

    def __init__(self):
        self.__factory = None

        "Manually takes the OS as input. In a real implementation, would use the platform import to check it."
        opsys = input("Enter OS: ").upper()

        if(opsys not in self.supportedOSDict.keys()):
            print("Operating system not supported. Supported operating systems:", list(self.supportedOSDict.keys()))
            return
        
        "Creates a factory for the given OS, storing it in the factory attribute"
        print(f"Creating a factory for {opsys} OS")
        self.__factory = self.supportedOSDict[opsys]()

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
