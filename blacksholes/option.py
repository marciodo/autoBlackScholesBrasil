import datetime


class Option():
    def __init__(self, symbol, strike, expirationDate, price=0.0):
        if isinstance(symbol, basestring):
            self.symbol = symbol
        else:
            raise TypeError("symbol must be a string with the format cccccnn",
                            ", c meaning character and n a number.")
        if isinstance(strike, float):
            self.strike = strike
        else:
            raise TypeError("strike must be a number.")
        if isinstance(expirationDate, datetime.date):
            self.expirationDate = expirationDate
        else:
            raise TypeError("expirationDate must be a date.")
        if isinstance(price, float):
            self.price = price
        else:
            raise TypeError("price must be a number.")
