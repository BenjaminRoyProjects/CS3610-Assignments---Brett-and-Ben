#CS3610 Assignment #7
#December 15, 2024
#Brett and Ben
#StockSubscriber

from SubscriberInt import SubscriberInt
from typing import Dict, Type

#Concrete subscriber class
#A subscriber to be added to a trader's subscriber list.
class StockSubscriber(SubscriberInt):
    def __init__(self, name):
        self.__name = name
        self.__stockData = {} #The subscriber's personal stock price dictionary.
    
    def __str__(self):
        return (f"Subscriber {self.__name}")
    
    #Update the subscriber's copy of the stock value data
    #Parameters:
    #   stockvalues: {String, Float}. A copy of the trader's stock data dictionary, to be used to update the subscriber's personal dictionary.
    #Returns: Nothing.
    def update(self, stockvalues:Dict[str,float], changedstock: Type[str]=""):
        if changedstock == "": #If an empty string is given for the stock name, add the entire dictionary
            for stock in stockvalues.keys():
                self.__stockData[stock] = stockvalues[stock] #Update each individual entry so a subscriber can have multiple traders
                print(f"Updated {self.__name}'s {stock} stock value to: {stockvalues[stock]}")
        else: #Update only the stock that changed
            self.__stockData[changedstock] = stockvalues[changedstock]
            print(f"Updated {self.__name}'s {changedstock} stock value to: {stockvalues[changedstock]}")

    #Remove an entry from the subscriber's stock data dictionary
    #Parameters:
    #   stockID: String. The name of the stock to be removed as it appears in the subscriber's dictionary.
    #Returns: Nothing.
    def removeStock(self, stockID: Type[str]):
        try:
            del self.__stockData[stockID]
        except ValueError:
            print(f"Failed to remove stock data from {self.__name}: Stock data does not exist.")

    #Print the current contents of the subscriber's stock data dictionary.
    #Parameters: None.
    #Returns: Nothing.
    def printStockData(self):
        keys = self.__stockData.keys()
        if len(keys) == 0: #No data in the subscriber's dictionary
            print(f"{self.__name} has no stock data.")
        else: #Some data in the subscriber's dictionary
            print(f"{self.__name} stock data:")
        for stock in self.__stockData.keys():
            print(f"{stock}: {self.__stockData[stock]}") #Print each stock name and value
        print()
