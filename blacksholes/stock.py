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

    def buyOption(self, optSymbol, price, strike=None, expirationDate=None):
        if strike is None and expirationDate is None:
            # So, we are buying an option that is already inside our list
            # of observed options.
            observedOption = self.__observedOptions[optSymbol]
            observedOption.price = price
            self.__boughtOptions[optSymbol] = observedOption
            del(self.__observedOptions[optSymbol])
        else:   # We are buying a new option that was not being observed.
                # Check to see if option actually is not in observed list
            if self.__observedOptions in optSymbol:
                raise buyError("Option is already in observed list")
                newOption = option.Option(optSymbol, strike, expirationDate,
                                          price)
                self.__boughtOptions[optSymbol] = newOption

    @property
    def boughtOptions(self):
        return self.__boughtOptions


class buyError(StandardError):
    """Exception raised for errors when buying a market item."""
    pass
