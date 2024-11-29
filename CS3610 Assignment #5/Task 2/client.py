from Application import Application
from MacFactory import MacFactory
from WinFactory import WinFactory

"Static dictionary of supported operating systems and their corresponding factories."
supportedOSDict = {"WINDOWS": WinFactory, "MAC": MacFactory}

"Manually takes the OS as input. In a real implementation, would use the platform import to check it."
while(True):
    opsys = input("Enter OS: ").upper()
    if(opsys not in self.supportedOSDict.keys()):
        print("Operating system not supported. Supported operating systems:", list(self.supportedOSDict.keys()))
    else:
        break

"Create the factory for the OS and make an Application using it"
print(f"Creating a factory for {opsys} OS")
app1 = Application(self.supportedOSDict[opsys]())
