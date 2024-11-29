from GUIFactory import GUIFactory

class WinFactory(GUIFactory):
    "A concrete factory extending the abstract GUIFactory. Creates only Windows elements."

    def createButton(self) -> Button:
        print("Creating a Windows button...")
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        print("Creating a Windows checkbox...")
        return WinCheckbox()