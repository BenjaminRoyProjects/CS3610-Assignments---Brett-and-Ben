#Car
#CS3610 Assignment #5
#Brett and Ben
#Dec 6, 2024

class Car:
  "A concrete product class."
  
  def __init__(self) -> None:
    self.__name = "Car"
    self.__components = []

  def add(self, component):
    print(f"Adding {component} to {self.__name}")
    self.__components.append(component)
    print(f"Current components: {self.__components}")

  def showComponents(self):
    print(f"There are {len(self.__components)} components in {self.__name}.")
    if len(self.__components) > 0:
      print("Components: ", end="")
      for component in self.__components:
        print(f"{component} ", end="")
      print("")
