from Typing import Type

class Director:
    "Class usable by client code to automatically control builders."

    def __init__(self):
        pass

    def makeSUV(self, builder):
        builder.reset()
        builder.setSeats("4")
        builder.setEngine("SUVEngine")
        builder.setTripComputer()
        builder.setGPS()

    def makeSportsCar(self, builder):
        builder.reset()
        builder.setSeats("2")
        builder.setEngine("SportEngine")
        builder.setTripComputer()
        builder.setGPS()