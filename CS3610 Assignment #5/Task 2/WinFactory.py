#WinFactory
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from GUIFactory import GUIFactory
from Button import Button
from WinButton import WinButton
from Checkbox import Checkbox
from WinCheckbox import WinCheckbox

class WinFactory(GUIFactory):
    #A concrete factory extending the abstract GUIFactory. Creates only Windows elements.

    def createButton(self) -> Button:
        #Creates and returns a windows button
        print("Creating a Windows button...")
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        #Creates and returns a windows checkbox
        print("Creating a Windows checkbox...")
        return WinCheckbox()
