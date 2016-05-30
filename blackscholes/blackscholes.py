from datetime import date
import datetime
import numpy
import pkg_resources
import yaml
import scipy.stats
from option import optionType
from numpy import datetime64
from numpy import timedelta64

# Read holiday file once when the import is done, to reduce time
resource_package = __name__
try:
    holidayFile = pkg_resources.resource_string(resource_package,
                                                'SaoPauloHolidays_numpy.yml')
    holidaysStr = yaml.load(holidayFile)
except:
    print('Holiday file not found.')
finally:
    holidays = []
    for holidayStr in holidaysStr:
        #year = holidayStr[0]
        #month = holidayStr[1]
        #day = holidayStr[2]
        #holidays.append(date(year, month, day))
        holidays.append(datetime64(holidayStr))
        #print datetime64(str(year) + "-0" + str(month) + "-0" + str(day))


def calcExpectedPrices(stock, interest):
    prices = {}
    interest /= 100.0
    histVolatility = stock.volatility / 100.0

    for observedOption in stock.observedOptions:
        option = stock.observedOptions[observedOption]
        strike = option.strike
        expirationDate = option.expirationDate

        lifetime = numpy.busday_count(date.today(), expirationDate +
                                      timedelta64(1, 'D'),
                                      '1111100', holidays)
        lifetime /= 252.0

        presentValue = strike * numpy.exp(-interest * lifetime)
        stHalf = histVolatility * numpy.power(lifetime, 0.5)
        d1 = (numpy.log(stock.price / strike) +
              (interest + histVolatility * histVolatility / 2) * lifetime) / \
            stHalf
        d2 = d1 - stHalf
        delta = scipy.stats.norm.cdf(d1)
        # print delta
        norm_d2_PV = scipy.stats.norm.cdf(d2) * presentValue
        # print norm_d2_PV
        callExpectedPrice = round(delta * stock.price - norm_d2_PV, 2)
        if option.type == optionType.PUT:
            putExpectedPrice = round(callExpectedPrice + presentValue -
                                     stock.price, 2)
            prices[option.symbol] = putExpectedPrice
        else:
            prices[option.symbol] = callExpectedPrice

    return prices
