#CS3610 Assignment #7
#December 15, 2024
#Brett and Ben
#StockTrader

from typing import Type
import random
from StockSubscriber import StockSubscriber
from SubscriberInt import SubscriberInt

#Publisher class
class StockTrader:
    def __init__(self):
        self.__subscribers = set() #Implemented as a set to prevent duplicate subscriptions
        self.__stockData = {} #Dictionary of floats. Each float holds the price for a particular stock. Stock names are the keys.

    #Add a subscriber to the trader's subscriber set so it will receive stock price updates, and add the current version of the trader's stock data to the subscriber.
    #Parameters:
    #   subscriber: StockSubscriber. The subscriber to be added to the trader's subscriber storage.
    #Returns: Nothing.
    def addSubscriber(self, subscriber: Type[SubscriberInt]):
        print(f"Adding {subscriber}...")
        if subscriber in self.__subscribers:
            print("Addition failed. This account is already subscribed.\n")
        else:
            self.__subscribers.add(subscriber)
            subscriber.update(self.__stockData) #Update the individual subscriber, not every subscriber
            print("Addition successful.\n")

    #Remove a subscriber from the trader's subscriber set, and remove this trader's tracked stocks from the subscriber's dictionary.
    #Parameters:
    #   subscriber: StockSubscriber. The subscriber to be removed from the trader's subscriber storage.
    #Returns: Nothing.
    def removeSubscriber(self, subscriber: Type[SubscriberInt]):
        print(f"Removing {subscriber}...")
        try:
            self.__subscribers.remove(subscriber) #Remove subscriber from trader's set
        except KeyError:
            print("Removal failed: No subscriber with that ID.\n")
        else:
            #Remove each piece of data from this trader from the subscriber's dictionary
            for stock in self.__stockData:
                subscriber.removeStock(stock)
            print("Removal successful.\n")

    #Send a copy of the updated stockData dictionary to every subscriber
    #Parameters: None.
    #Returns: Nothing.
    def updateSubscribers(self, changedstock: Type[str]=""):
        print("Updating subscriber data...")
        if len(self.__subscribers) == 0:
            print("No subscribers to update.")
        else:
            for sub in self.__subscribers:
                sub.update(self.__stockData, changedstock)

    #Update the value of a current stock or add a new stock with an initial value
    #Parameters:
    #   stockID: String. The name of the stock being changed as it appears in the trader's dictionary.
    #   newValue: Float. The new value to be assigned to the stock in the trader's dictionary.
    #Returns: Nothing.
    def stockChange(self, stockID: Type[str], newValue: Type[float]):
        if stockID in self.__stockData.keys():
            print(f"Changing value of {stockID} stock from {self.__stockData[stockID]} to {newValue}.")
        else:
            print(f"Adding new stock {stockID} with value {newValue}.")
        self.__stockData[stockID] = newValue
        self.updateSubscribers(stockID)
        print()

    #Simulate random stock market fluctuations for testing purposes
    #Parameters:
    #   fluctchance: Integer, Minimum 1. Determines the odds of each stock having its value changed. The higher this value, the less likely each stock is to change.
    #   fluctrange: Integer, Minimum 1. Determines the upper and lower bound for the random value change for each stock that is being modified. The range of alteration is +- this number.
    #Returns: Nothing.
    def marketFluct(self, fluctchance: Type[int], fluctrange: Type[int]):
        for stock in self.__stockData:
            #Generate two random numbers. If they are equal, change the value of the stock
            try:
                randomvalue = random.randrange(1, fluctchance)
                randomvalue2 = random.randrange(1, fluctchance)
            except ValueError: #If fluctrange has a value of 1
                randomvalue = 1
                randomvalue2 = 1
            if randomvalue == randomvalue2:
                print(f"{stock} stock value updated...")
                #Add or subtract a random amount from the stock's value
                temp = self.__stockData[stock]
                rand = int(random.randrange((fluctrange * -1), (fluctrange)))
                if rand == 0: #Don't want to update a stock to the exact same value
                    rand = 1
                temp += rand
                self.stockChange(stock, temp)