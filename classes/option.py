import stock

class Option():
  def __init__(self, symbol, stock, strike):
    self.symbol = symbol
    self.stock = stock
    self.strike = strike
    
bbas3 = stock.Stock("Banco do Brasil", "BBAS3")
bbase74 = Option("BBASE74", bbas3, 27.4)

bbase74.stock.setPrice(25)
bbase74.stock.setVolatility(85)

print bbase74.symbol
print bbase74.stock.name
print bbase74.stock.symbol
print bbase74.stock.getPrice()
print bbase74.stock.getVolatility()
print bbase74.strike