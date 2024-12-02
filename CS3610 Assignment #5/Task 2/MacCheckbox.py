from Checkbox import Checkbox

class MacCheckbox(Checkbox):
    "Concrete product class."

    def __init__(self):
        self.__isChecked = False

    @property
    def isChecked(self) -> bool:
        "Getter for isChecked."
        return self.__isChecked

    def check(self) -> None:
        "Checks the checkbox."
        self.__isChecked = True

    def __str__(self):
        return "MacCheckbox"