from Button import Button

class WinButton(Button):
    "Concrete product class."

    def __init__(self):
        "Statement printed on button press."
        self.__statement = ""

    @property
    def statement(self) -> None:
        "Getter for statement."
        return self.__statement

    @statement.setter
    def statement(self, statement: str) -> None:
        "Setter for statement."
        self.__statement = statement

    def press(self) -> None:
        "Presses the button."
        print(self.__statement)

    def __str__(self):
        return "WinButton"