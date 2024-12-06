from document import document

class txtDocument(document):
    def __init__(self):
        self.objType = "TXT doc"
    def create(self):
        return f"TXT document has been created"