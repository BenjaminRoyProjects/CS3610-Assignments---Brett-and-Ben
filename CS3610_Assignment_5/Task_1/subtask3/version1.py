from pdfDocumentCreator import pdfDocumentCreator
from wordDocumentCreator import wordDoucmentCreator

class version1:
    def create(self, testDocs):
        for name in testDocs:
            try:
                if name.lower() == 'pdf':
                    creator = pdfDocumentCreator()
                elif name.lower() == 'word':
                    creator = wordDoucmentCreator()
                else:
                    raise Exception("I cant make this object")
                res = creator.factory_method()
                if res:
                    print(res.objType)
            except Exception as _e:
                print(_e)
        return None