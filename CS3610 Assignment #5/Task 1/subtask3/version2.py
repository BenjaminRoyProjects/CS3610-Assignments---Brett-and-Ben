from documentCreator import documentCreatorClass, pdfDocument, wordDocument, txtDocument
import documentCreator

documentCreator.docTypes = {"pdf":pdfDocument, "word":wordDocument, "txt":txtDocument}

class version2():
    def create_document(objType: str):
        return documentCreatorClass.create_document(objType)