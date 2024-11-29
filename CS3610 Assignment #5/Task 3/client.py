from Director import Director
from Builder import Builder
from CarBuilder import CarBuilder

director = Director()
builder = CarBuilder()
director.makeSportsCar(builder)
car = builder.getResult()