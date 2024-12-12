#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#StockSubscriber

from SubscriberInt import SubscriberInt
from typing import Dict

#concrete subscriber class
class StockSubscriber(SubscriberInt):
    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return (f"Subscriber {self.__name}")
    
    def update(self, context:Dict[str,float]):
        keys = context.keys()
        for i in keys:
            print(f"Updated {self.__name}'s {i} stock value to: {context[i]}")
    
