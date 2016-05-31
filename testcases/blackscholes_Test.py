# coding: utf-8
import unittest
import datetime
import yaml
from blackscholes.stock import Stock
from blackscholes import blackscholes
from numpy import busday_offset
from numpy import datetime64


class BlachscholesTest(unittest.TestCase):

    def test_openHolidayFile(self):
        self.assertEqual(datetime64('2001-01-01'), blackscholes.holidays[0])
        self.assertEqual(datetime64('2078-12-25'),
                         blackscholes.holidays[935])

    def test_getExpectedPriceCall_ObservedList(self):
        itub4 = Stock('Itaú', 'ITUB4')
        itub4.price = 30.08
        itub4.volatility = 49.25
        # For automatic test purposes we need to calculate the expiration date
        # from today to get the same result every time.
        businessDays = 19
        expirationDate = busday_offset(datetime.date.today(), businessDays,
                                       'backward', '1111100',
                                       blackscholes.holidays)
        itub4.observeOption('ITUBF8', 33.81, expirationDate)
        expectedPrices = blackscholes.calcExpectedPrices(itub4, 14.25)
        self.assertEqual(0.57,
                         expectedPrices['ITUBF8'])

    def test_getExpectedPricePut_ObservedList(self):
        petr4 = Stock('Petrobrás', 'PETR4')
        petr4.price = 8.9
        petr4.volatility = 70.6
        # For automatic test purposes we need to calculate the expiration date
        # from today to get the same result every time.
        businessDays = 19
        expirationDate = busday_offset(datetime.date.today(), businessDays,
                                       'backward', '1111100',
                                       blackscholes.holidays)
        petr4.observeOption('PETRR76', 7.6, expirationDate)
        expectedPrices = blackscholes.calcExpectedPrices(petr4, 14.25)
        self.assertEqual(0.17,
                         expectedPrices['PETRR76'])

if __name__ == '__main__':
    unittest.main()
