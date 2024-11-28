from documentCreator import documentCreator

testDocs = ['pdf','txt',"word",'word','txt']
for name in testDocs:
    res = documentCreator.create_document(name)
    if res:
        print(res.objType)