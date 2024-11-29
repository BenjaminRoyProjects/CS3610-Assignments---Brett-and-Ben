class Car:
  "A concrete product class."
  
  def __init__(self) -> None:
    self.__name = "Car"
    self.__components = []

  def add(self, component):
    print(f"Adding {component} to {self.__name}")
    self.__components.append(component)
    print(f"Current components: {self.__components}

  def showComponents(self):
    print(f"There are {len(self.__components)} components in {self.__name}.")
    print("Components: ", end="")
    for component in self.__components:
      print(f"{component} ", end="")
