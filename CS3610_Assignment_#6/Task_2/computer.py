from hdd import hdd
from opticalDiscReader import opticalDiscReader
from powerSupply import powerSupply
from ram import ram
from sensors import sensors
from videoCard import videoCard

#this is the facade class
class computer():
    def turnOn():
        powerSupply.applyPower()
        sensors.checkVoltage()
        sensors.checkPSUTemperature()
        sensors.checkGPUTemperature()
        powerSupply.powerVideoCard()
        videoCard.start()
        videoCard.checkConnection()
        sensors.checkRAMTemperature()
        powerSupply.powerRAM()
        ram.start()
        ram.analysis()
        videoCard.ramData()
        powerSupply.powerOpticalDiscReader()
        opticalDiscReader.start()
        opticalDiscReader.checkDisc()
        videoCard.discReaderData()
        powerSupply.powerHDD()
        hdd.start()
        hdd.checkBoot()
        videoCard.hddData()
        sensors.checkkAllTemperature()
        
    def turnOff():
        hdd.stop()
        ram.stop()
        videoCard.stop()
        opticalDiscReader.stop()
        powerSupply.stopPowerVideoCard()
        powerSupply.stopPowerRam()
        powerSupply.stopPowerOpticalDiscReader()
        powerSupply.stopPowerHDD()
        sensors.checkVoltage()
        powerSupply.stopPower()