#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#SubscriberInt

from abc import abstractmethod,ABC

#subscriber class
class SubscriberInt(ABC):
    
    @abstractmethod
    def update(self,context):
        pass
