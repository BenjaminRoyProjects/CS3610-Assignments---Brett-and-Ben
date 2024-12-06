from documentCreator import documentCreator
from pdfDocumentCreator import pdfDocumentCreator
from wordDocumentCreator import wordDoucmentCreator
from txtDocumentCreator import txtDocumentCreator

testDocs = ['pdf','txt',"word",'word','txt']

for name in testDocs:
    if name.lower() == 'pdf':
        creator = pdfDocumentCreator()
    elif name.lower() == 'word':
        creator = wordDoucmentCreator()
    elif name.lower() == 'txt':
        creator = txtDocumentCreator()
    res = creator.factory_method()
    if res:
        print(res.objType)