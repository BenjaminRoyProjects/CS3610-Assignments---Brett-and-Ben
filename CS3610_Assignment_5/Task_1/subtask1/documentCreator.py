from abc import ABC, abstractmethod
from document import document

class documentCreator(ABC):
    
    @staticmethod
    def create_document(objType: str) -> str:
        pass
    
    @abstractmethod
    def factory_method(self) -> document:
        pass