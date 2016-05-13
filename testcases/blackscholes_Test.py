# coding: utf-8
import unittest
import datetime
from blackscholes.stock import Stock
from blackscholes import blackscholes


class BlachscholesTest(unittest.TestCase):

    def test_getImpliedVolatility1ObservedCall(self):
        itub4 = Stock("Itaú", "ITUB4")
        itub4.price = 30.4
        itub4.volatity = 49.25
        itub4.observeOption("ITUBF8", 33.81, datetime.date(2016, 6, 20))
        observedImpliedVolatility = \
            blackscholes.getObservedImpliedVolatility(itub4, 14.25)
        self.assertEqual(65.25,
                         observedImpliedVolatility['ITUBF8'].impliedVolatility)

if __name__ == '__main__':
    unittest.main()
