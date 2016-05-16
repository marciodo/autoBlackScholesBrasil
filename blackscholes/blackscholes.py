from datetime import date
import numpy
import pkg_resources
import yaml

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
        option = stock.observedOptions[observedOption]
        strike = option.strike
        expirationDate = option.expirationDate

        #holiday = [date(2016, 5, 16), date(2016, 9, 7)]

        lifetime = numpy.busday_count(date.today(), expirationDate,
                                      '1111100', holidays)
        lifetime += 1
        print lifetime
        print lifetime / 252.0
        #presentValue = 

    return {"ITUBF8": 65.25}
