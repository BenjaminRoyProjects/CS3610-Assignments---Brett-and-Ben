#MacFactory
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from GUIFactory import GUIFactory
from Button import Button
from MacButton import MacButton
from Checkbox import Checkbox
from MacCheckbox import MacCheckbox

class MacFactory(GUIFactory):
    #A concrete factory extending the abstract GUIFactory. Creates only Mac elements.

    def createButton(self) -> Button:
        #Creates and returns a mac button
        print("Creating a Mac button...")
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        #Creates and returns a mac checkbox
        print("Creating a Mac checkbox...")
        return MacCheckbox()
