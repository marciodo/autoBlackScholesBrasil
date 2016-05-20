from datetime import date
import numpy
import pkg_resources
import yaml
import scipy.stats

# Read holiday file once when the import is done to reduce time
resource_package = __name__
try:
    holidayFile = pkg_resources.resource_string(resource_package,
                                                "SaoPauloHolidays.yml")
    holidaysStr = yaml.load(holidayFile)
except:
    print("Holiday file not found.")
finally:
    holidays = []
    for holidayStr in holidaysStr:
        year = holidayStr[0]
        month = holidayStr[1]
        day = holidayStr[2]
        holidays.append(date(year, month, day))


def getObservedImpliedVolatility(stock, interest):
    for observedOption in stock.observedOptions:
        interest /= 100.0
        option = stock.observedOptions[observedOption]
        strike = option.strike
        expirationDate = option.expirationDate
        histVolatility = stock.volatility / 100.0

        #holiday = [date(2016, 5, 16), date(2016, 9, 7)]

        lifetime = numpy.busday_count(date.today(), expirationDate,
                                      '1111100', holidays)
        lifetime += 1
        lifetime /= 252.
        print lifetime
        presentValue = strike * numpy.exp(-interest * lifetime)
        print presentValue
        stHalf = histVolatility * numpy.power(lifetime, 0.5)
        print stHalf
        d1 = (numpy.log(stock.price / strike) +
              (interest + histVolatility * histVolatility / 2) * lifetime) / \
            stHalf
        print d1
        d2 = d1 - stHalf
        print d2
        delta = scipy.stats.norm(0, 1).cdf(d1)
        print delta

    return {"ITUBF8": 65.25}
