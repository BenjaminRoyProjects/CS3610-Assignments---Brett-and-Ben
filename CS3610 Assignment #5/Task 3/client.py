from director import Director
from builder import Builder
from carBuilder import CarBuilder
from manualBuilder import ManualBuilder

director = Director()
builder = CarBuilder()
mBuilder = ManualBuilder()
#director.makeSUV(builder)
director.makeSUV(mBuilder)
manual = builder.getResult()