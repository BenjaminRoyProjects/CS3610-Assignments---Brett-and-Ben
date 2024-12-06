from documentCreator import documentCreator
from pdfDocument import pdfDocument

class pdfDocumentCreator(documentCreator):
    def factory_method(self):
        return pdfDocument()