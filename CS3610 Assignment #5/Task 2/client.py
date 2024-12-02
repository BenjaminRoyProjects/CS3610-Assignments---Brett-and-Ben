#Client
#CS3610 Assignment #5
#Brett and Ben
#Dec 2, 2024

from Application import Application
from MacFactory import MacFactory
from WinFactory import WinFactory

#Static dictionary of supported operating systems and their corresponding factories.
supportedOSDict = {"WINDOWS": WinFactory, "MAC": MacFactory}

#Manually takes the OS as input. In a real implementation, would use the platform import to check it.
opsys = None
while(True):
    opsys = input("Enter OS: ").upper()
    if(opsys not in supportedOSDict.keys()):
        print("Operating system not supported. Supported operating systems: ", end="")
        for os in list(supportedOSDict.keys()):
            print(f"{os} ", end="")
        print("")
    else:
        break
print(f"Creating a factory for {opsys} OS")
factory = supportedOSDict[opsys]()
'''
if opsys = "MAC":
    factory = MacFactory()
if opsys = "WINDOWS":
    factory = WinFactory()
'''

#Create and use an Application with your factory
app1 = Application(factory)
app1.createUI()
app1.paint()

#cd CS3610\ Assignment\ #5/Task\ 2/
#python client.py