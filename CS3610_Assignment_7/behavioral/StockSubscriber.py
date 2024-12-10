#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#StockSubscriber

from SubscriberInt import SubscriberInt

#concrete subscriber class
class StockSubscriber(SubscriberInt):
    def __init__(self, name):
        self.__subject = None
        self.__name = name
    
    def __str__(self):
        print(f"Subscriber {self.__name}")
    
    def update(self, context):
        print(f"stock {self.__subject} is {context}")
    
