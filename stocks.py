class Stock():
    def __init__(self, symbol, openPrice, highPrice, lowPrice, volume):
        self.symbol = symbol
        self.openPrice = openPrice
        self.highPrice = highPrice
        self.lowPrcie = lowPrice
        self.volume = volume
        self.stockPriceList = []
        self.stockDate = []

    def addPrice(self, price, date):
        self.stockPriceList.append(price)
        self.stockDate.append(date)
        
        


