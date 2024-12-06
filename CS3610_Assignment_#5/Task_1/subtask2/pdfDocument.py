from document import document

class pdfDocument(document):
    def __init__(self):
        self.objType = "PDF doc"
    def create(self):
        return f"PDF document has been created"