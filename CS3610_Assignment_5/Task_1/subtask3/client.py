from version1 import version1
from version2 import version2

testDocs = ['pdf','txt',"word",'word','txt','png']
version = version1()
#version = version2()

version.create(testDocs)