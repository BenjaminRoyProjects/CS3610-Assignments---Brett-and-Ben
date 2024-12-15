#CS3610 Assignment #7
#December 15, 2024
#Brett and Ben
#Client

from StockSubscriber import StockSubscriber
from StockTrader import StockTrader

#Create subscribers and trader.
sub1 = StockSubscriber('test1')
sub2 = StockSubscriber('test2')
sub3 = StockSubscriber('test3')
trader1 = StockTrader()

#Add one stock value. Newly added subscribers should immediately inherit this data.
trader1.stockChange("IBM", 34.7)

#Add the subscribers to the trader's internal set.
trader1.addSubscriber(sub1)
trader1.addSubscriber(sub2)
sub2.printStockData()
trader1.addSubscriber(sub3)

#Attempt to add the same subscriber again
trader1.addSubscriber(sub3)

#Remove one of the subscribers from the trader's internal set.
trader1.removeSubscriber(sub2)
sub2.printStockData()

#Change the value of several stocks. Attempting to change the value of a stock not in the trader will add it.
trader1.stockChange("IBM", 21.9)
trader1.stockChange("Amazon", 89.6)
trader1.stockChange("Facebook", 71.3)

#Mimic natural stock market fluctuations
trader1.marketFluct(1, 10)
sub3.printStockData()

#Create a second trader and add a subscriber to it as well
trader2 = StockTrader()
trader2.stockChange("Microsoft", 94.7)
trader2.addSubscriber(sub3)
sub3.printStockData()