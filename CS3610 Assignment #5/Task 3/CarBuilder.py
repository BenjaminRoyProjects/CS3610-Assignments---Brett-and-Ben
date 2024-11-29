from Builder import Builder
from Typing import Type

class CarBuilder(Builder):
  "Concrete builder class for cars."

  def __init__(self):
    self.__car = Car()

  @property
  def car(self) -> Car:
    return self.__car

  @car.setter
  def car(self, newcar: Type[Car]) -> None:
    self.__car = newcar
  
  def reset() -> None:
    self.__car = Car()
    
  def setSeats(number) -> None:
    pass

  def setEngine(engine) -> None:
    pass

  def setTripComputer(number) -> None:
    pass

  def setGPS(number) -> None:
    pass
