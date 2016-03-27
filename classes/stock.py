class Stock():
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol
    
    
  def setPrice(self, price):
    self.price = price
    
    
  def getPrice(self):
    return self.price


  def setVolatility(self, volatility):
    self.volatility = volatility
    
    
  def getVolatility(self):
    return self.volatility