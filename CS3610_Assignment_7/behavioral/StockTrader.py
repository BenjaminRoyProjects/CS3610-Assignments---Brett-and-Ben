#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#StockTrader

from typing import Type
#from StockSubscriber import StockSubscriber

class StockTrader:
    def __init__():
        self.__subscribers = set() #Implemented as a set to prevent duplicate subscriptions

    def addSubscriber(subscriber: Type[SubscriberInt]):
        print(f"Removing subscriber {subscriber}...", end="")
        self.__subscribers.add(subscriber)

    def removeSubscriber(subscriber: Type[SubscriberInt]):
        self.__subscribers.remove(subscriber)

class SubscriberInt():
    pass
class StockSubscriber(SubscriberInt):
    pass

trader1 = StockTrader()
sub1 = StockSubscriber()
trader1.addSubscriber(sub1)