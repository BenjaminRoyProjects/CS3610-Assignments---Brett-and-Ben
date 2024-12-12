#CS3610 Assignment #7
#December 16, 2024
#Brett and Ben
#Client

from StockSubscriber import StockSubscriber
from StockTrader import StockTrader


tmpObserver = StockSubscriber('test1')
tmp2Observer = StockSubscriber('test2')
tmp3Observer = StockSubscriber('test3')
tmpTrader = StockTrader()
tmpTrader.addSubscriber(tmpObserver)
tmpTrader.addSubscriber(tmp2Observer)
tmpTrader.addSubscriber(tmp3Observer)

tmpTrader.removeSubscriber(tmp2Observer)

tmpTrader.stockChange("IBM", 34.7)
tmpTrader.stockChange("IBM", 21.9)
tmpTrader.stockChange("Amazon", 89.6)
tmpTrader.stockChange("Facebook", 71.3)
tmpTrader.marketFluct()