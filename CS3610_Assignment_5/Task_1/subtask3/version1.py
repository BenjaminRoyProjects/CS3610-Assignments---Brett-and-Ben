from documentCreator import documentCreatorClass, pdfDocument, wordDocument
import documentCreator

documentCreator.docTypes = {"pdf":pdfDocument, "word":wordDocument}

class version1():
    def create_document(objType: str):
        return documentCreatorClass.create_document(objType)