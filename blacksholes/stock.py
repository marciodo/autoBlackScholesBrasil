import option

class Stock():
    def __init__(self, name, symbol):
	self.name = name
	self.symbol = symbol
	self.price = 0
	self.volatility = 0
	self.__observedOptions = {}
	self.__boughtOptions = {}
    
    
    def observeOption(self, optSymbol, strike, expirationDate):
	newOption = option.Option(optSymbol, strike, expirationDate)
	self.__observedOptions[optSymbol] = newOption
	

    @property
    def observedOptions(self):
	return self.__observedOptions
    
    
    def buyOption(self, optSymbol, price):
	option = self.__observedOptions[optSymbol]
	option.price = price
	self.__boughtOptions[optSymbol] = option
	del(self.__observedOptions[optSymbol])
	
	
    def buyOption(self, optSymbol, strike, expirationDate, price):
	newOption = option.Option(optSymbol, strike, expirationDate, price)
	self.__observedOptions[optSymbol] = newOption
	

    @property
    def boughtOptions(self):
	return self.__boughtOptions
    