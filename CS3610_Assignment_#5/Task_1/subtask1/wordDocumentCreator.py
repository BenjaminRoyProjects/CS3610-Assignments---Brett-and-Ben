from documentCreator import documentCreator
from wordDocument import wordDocument

class wordDoucmentCreator(documentCreator):
    def factory_method(self):
        return wordDocument.create()