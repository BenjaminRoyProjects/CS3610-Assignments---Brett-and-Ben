#client
#CS3610 Assignment #5
#Brett and Ben
#Dec 6, 2024

from Director import Director
from Builder import Builder
from CarBuilder import CarBuilder
from CarManualBuilder import ManualBuilder

builder1 = CarBuilder()
director1 = Director(builder1) #Car -uilding director
director1.makeSportsCar()
car1 = director1.builder.getResult()
car1.showComponents()

print("")

builder2 = ManualBuilder()
director1.builder = builder2 #Manual-building director
director1.makeSUV()
manual1 = director1.builder.getResult()
manual1.showComponents()

#cd CS3610\ Assignment\ #5/\Task\ 3
#python client.py
