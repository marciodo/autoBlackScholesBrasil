from datetime import date
import numpy


def getObservedImpliedVolatility(stock, interest):
    for observedOption in stock.observedOptions:
        option = stock.observedOptions[observedOption]
        strike = option.strike
        expirationDate = option.expirationDate

        holiday = [date(2016, 5, 16), date(2016, 9, 7)]

        lifetime = numpy.busday_count(expirationDate, date.today(),
                                      '1111100', holiday)
        print lifetime / 365.0
        #presentValue = 

    return {"ITUBF8": 65.25}
