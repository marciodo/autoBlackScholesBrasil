from blacksholes import stock
import datetime

bbas3 = stock.Stock("Banco do Brasil", "BBAS3")
bbas3.price = 21
bbas3.volatility = 95
bbas3.observeOption("BBASE74", 27.4, datetime.date(2016, 4, 28))

print bbas3.symbol
print bbas3.name
print bbas3.price
print bbas3.volatility
print (bbas3.observedOptions)
bbas3.buyOption("BBASE74", 0.75)
print (bbas3.observedOptions)
print (bbas3.boughtOptions["BBASE74"].price)

bbas3.buyOption("BBASE72", 24.7, datetime.date(2016, 4, 28), 0.35)