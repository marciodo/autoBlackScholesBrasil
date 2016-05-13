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
        if optSymbol in self.__observedOptions:
            raise ObserveError("Option is already in observed list")
        newOption = option.Option(optSymbol, strike, expirationDate)
        self.__observedOptions[optSymbol] = newOption

    @property
    def observedOptions(self):
        return self.__observedOptions

    def buyOption(self, optSymbol, price, strike=None, expirationDate=None):
        if strike is None and expirationDate is None:
            if optSymbol not in self.__observedOptions:
                raise BuyError("Option is not being oberved. Please tell us "
                               "its strike and expiration date.")
            # So, we are buying an option that is already inside our list
            # of observed options.
            observedOption = self.__observedOptions[optSymbol]
            observedOption.price = price
            self.__boughtOptions[optSymbol] = observedOption
            del(self.__observedOptions[optSymbol])
        else:   # We are buying a new option that was not being observed.
                # Check to see if option actually is not in observed list.
            if optSymbol in self.__observedOptions:
                raise BuyError("Option is already in observed list")
            else:
                newOption = option.Option(optSymbol, strike, expirationDate,
                                          price)
                self.__boughtOptions[optSymbol] = newOption

    @property
    def boughtOptions(self):
        return self.__boughtOptions


class BuyError(StandardError):
    """Exception raised for errors when buying a market item."""
    pass


class ObserveError(StandardError):
    """Exception raised for errors when observing an option."""
    pass
