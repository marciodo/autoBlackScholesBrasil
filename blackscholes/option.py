import datetime
import re
from enum import Enum


class optionType(Enum):
    CALL = 0
    PUT = 1


class Option():
    def __init__(self, symbol, strike, expirationDate, price=0.0):
        if isinstance(symbol, basestring):
            if re.match("[a-zA-Z]{4}[a-xA-X][0-9]{1,2}", symbol) is None:
                raise ValueError("symbol must have the format cccccn[n],"
                                 " c meaning a character, n a "
                                 "number and [n] an optional number.")
            self.symbol = symbol
        else:
            raise TypeError("symbol must be a string with the format "
                            "cccccn[n], c meaning a character, n a number and"
                            " [n] an optional number.")
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

        if self.symbol[4:5].upper() < 'M':
            self.type = optionType.CALL
        else:
            self.type = optionType.PUT
