from pdfDocumentCreator import pdfDocumentCreator
from wordDocumentCreator import wordDoucmentCreator
from txtDocumentCreator import txtDocumentCreator

class version2:
    def create(self, testDocs):
        for name in testDocs:
            try:
                if name.lower() == 'pdf':
                    creator = pdfDocumentCreator()
                elif name.lower() == 'word':
                    creator = wordDoucmentCreator()
                elif name.lower() == 'txt':
                    creator = txtDocumentCreator()
                else:
                    raise Exception("I can't make this object")
                res = creator.factory_method()
                if res:
                    print(res.objType)
            except Exception as _e:
                print(_e)
        return None