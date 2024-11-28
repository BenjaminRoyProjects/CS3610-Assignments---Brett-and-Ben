from document import document

class wordDocument(document):
    def __init__(self):
        self.objType = "Word doc"
    def create(self,):
        return f"Word document has been created"