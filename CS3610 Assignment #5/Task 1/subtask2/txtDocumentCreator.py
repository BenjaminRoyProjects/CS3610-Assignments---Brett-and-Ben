from documentCreator import documentCreator
from txtDocument import txtDocument

class txtDocumentCreator(documentCreator):
    def factory_method(self):
        return txtDocument.create()