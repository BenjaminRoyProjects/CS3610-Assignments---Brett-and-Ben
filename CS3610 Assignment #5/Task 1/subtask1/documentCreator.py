from typing import Type, Self
from abc import ABC, abstractmethod
from pdfDocument import pdfDocument
from wordDocument import wordDocument,document

docTypes = {"pdf":pdfDocument, "word":wordDocument}

class documentCreator(ABC):
    @staticmethod
    def create_document(objType: str) -> str:
        try:
            if objType.lower() in docTypes.keys():
                return docTypes[objType]()
            else:
                raise Exception("This is not a valid document type")
        except Exception as _e:
            print(_e)
        return None
    
    @abstractmethod
    def factory_method(self) -> document:
        pass