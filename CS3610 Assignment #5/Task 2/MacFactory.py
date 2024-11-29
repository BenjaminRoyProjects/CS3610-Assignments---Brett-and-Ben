#from GUIFactory import GUIFactory

class MacFactory(GUIFactory):
    "A concrete factory extending the abstract GUIFactory. Creates only Mac elements."

    def createButton(self) -> Button:
        print("Creating a Mac button...")
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        print("Creating a Mac checkbox...")
        return MacCheckbox()