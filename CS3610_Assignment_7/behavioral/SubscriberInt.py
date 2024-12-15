#CS3610 Assignment #7
#December 15, 2024
#Brett and Ben
#SubscriberInt

from abc import abstractmethod,ABC
from typing import Dict, Type

#Subscriber interface
class SubscriberInt(ABC):
    
    #Update the subscriber's copy of the stock value data
    #Parameters:
    #   stockvalues: {String, Float}. A copy of the trader's stock data dictionary, to be used to update the subscriber's personal dictionary.
    #Returns: Nothing.
    @abstractmethod
    def update(self, stockvalues: Dict[str, float]):
        pass

    #Remove an entry from the subscriber's stock data dictionary
    #Parameters:
    #   stockID: String. The name of the stock to be removed as it appears in the subscriber's dictionary.
    #Returns: Nothing.
    @abstractmethod
    def removeStock(self, stockID: Type[str]):
        pass
