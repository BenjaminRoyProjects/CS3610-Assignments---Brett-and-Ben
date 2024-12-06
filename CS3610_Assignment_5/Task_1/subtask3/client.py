from version1 import version1
from version2 import version2

testDocs = ['pdf','txt',"word",'word','txt']
for name in testDocs:
    res = version1.create_document(name)
    if res:
        print(res.objType)
        
'''for name in testDocs:
    res = version2.create_document(name)
    if res:
        print(res.objType)
'''