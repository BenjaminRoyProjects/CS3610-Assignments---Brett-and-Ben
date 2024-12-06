from documentCreator import documentCreator

testDocs = ['pdf',"word",'word']
for name in testDocs:
    res = documentCreator.create_document(name)
    if res:
        print(res.objType)