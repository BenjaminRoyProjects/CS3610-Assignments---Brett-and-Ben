from abc import ABC, abstractmethod

class Builder(ABC):
  "Interface for builder classes."

  @abstractmethod
  def reset() -> None:
    pass

  @abstractmethod
  def setSeats(number) -> None:
    pass

  @abstractmethod
  def setEngine(engine) -> None:
    pass

  @abstractmethod
  def setTripComputer(number) -> None:
    pass

  @abstractmethod
  def setGPS(number) -> None:
    pass
