from abc import ABC, abstractmethod

class document():
    @abstractmethod
    def create(self, type) -> str:
        pass