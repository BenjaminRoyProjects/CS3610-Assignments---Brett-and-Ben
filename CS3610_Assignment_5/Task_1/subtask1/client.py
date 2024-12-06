from documentCreator import documentCreator
from pdfDocumentCreator import pdfDocumentCreator
from wordDocumentCreator import wordDoucmentCreator

testDocs = ['pdf',"word",'word']

for name in testDocs:
    if name.lower() == 'pdf':
        creator = pdfDocumentCreator()
    elif name.lower() == 'word':
        creator = wordDoucmentCreator()
    res = creator.factory_method()
    if res:
        print(res.objType)