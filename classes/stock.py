import option

class Stock():
    def __init__(self, name, symbol):
	self.name = name
	self.symbol = symbol
	self.price = 0
	self.volatility = 0
	self._option = []
    
    
    def addOption(self, optSymbol, strike, expirationDate):
	newOption = option.Option(optSymbol, strike, expirationDate)
	self._option.append(newOption)
	
	
    def getOptions(self):
	return self._option