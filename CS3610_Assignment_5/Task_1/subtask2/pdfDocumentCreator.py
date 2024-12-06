from documentCreator import documentCreator
from pdfDocument import pdfDocument

class pdfDocuementCreator(documentCreator):
    def factory_method(self):
        return pdfDocument.create()