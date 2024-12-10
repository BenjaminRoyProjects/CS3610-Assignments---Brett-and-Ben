#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#StockTrader

class SubscriberInt():
    def __str__(self):
        return "Subscriber"
class StockSubscriber(SubscriberInt):
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return f"Subscriber {self.__name}"
    def update(self, newdict):
        print(f"Subscriber {self.__name} updated with {newdict}.")

from typing import Type
import random
#from StockSubscriber import StockSubscriber

class StockTrader:
    #Serves as an upper bound to a random calculation used to simulate random market fluctuations. The higher it is, the fewer stock values will change. Minimum 1.
    __MARKETFLUCTUATION = 5 
    
    def __init__(self):
        self.__subscribers = set() #Implemented as a set to prevent duplicate subscriptions
        self.__stockData = {} #Dictionary of floats. Each float holds the price for a particular stock. Stock names are the keys.

    #Add a subscriber to the subscriber set
    def addSubscriber(self, subscriber: Type[SubscriberInt]):
        print(f"Adding {subscriber}...")
        if subscriber in self.__subscribers:
            print("Addition failed. A Stock Trader subscriber with this ID already exists.")
        else:
            self.__subscribers.add(subscriber)
            print("Addition successful.")

    #Remove a subscriber from the subscriber set
    def removeSubscriber(self, subscriber: Type[SubscriberInt]):
        print(f"Removing {subscriber}...")
        try:
            self.__subscribers.remove(subscriber)
        except KeyError:
            print("Removal failed: No Stock Trader subscriber with that ID.")
        else:
            print("Removal successful.")

    #Send a copy of the updated stockData dictionary to every subscriber
    def updateSubscribers(self):
        for sub in self.__subscribers:
            sub.update(self.__stockData)

    #Update the value of a current stock or add a new stock with an initial value
    def stockChange(self, stockID: Type[str], newValue: Type[float]):
        if stockID in self.__stockData.keys():
            print(f"Changing value of {stockID} to {newValue}.")
        else:
            print(f"Adding new stock {stockID} with value {newValue}.")
        self.__stockData[stockID] = newValue
        self.updateSubscribers()

    #Simulate random stock market fluctuations
    def marketFluct(self):
        for stock in self.__stockData:
            randomvalue = random.randrange(1, self.__MARKETFLUCTUATION)
            print(randomvalue)
            randomvalue2 = random.randrange(1, self.__MARKETFLUCTUATION)
            print(randomvalue2)
            if randomvalue == randomvalue2:
                print(f"Changing {stock}")
        


trader1 = StockTrader()
sub1 = StockSubscriber("Test1")
trader1.addSubscriber(sub1)
sub2 = StockSubscriber("Test2")
trader1.removeSubscriber(sub2)
trader1.addSubscriber(sub1)
trader1.stockChange("IBM", 34.7)
trader1.stockChange("IBM", 21.9)
trader1.stockChange("Amazon", 89.6)
trader1.stockChange("Facebook", 71.3)
trader1.marketFluct()