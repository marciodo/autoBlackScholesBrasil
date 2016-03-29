from blacksholes import stock
import datetime

bbas3 = stock.Stock("Banco do Brasil", "BBAS3")
bbas3.price = 21
bbas3.volatility = 95
bbas3.addOption("BBASE74", 27.4, datetime.date(2016, 4, 28))

print bbas3.symbol
print bbas3.name
print bbas3.price
print bbas3.volatility
options = bbas3.getObservedOptions()
print options