# coding: utf-8
import unittest
import datetime
from blacksholes.stock import Stock

""" Test list:
- Buy an unobserved option
- Observe 2 equal options
- Buy 2 equal options
- Try to buy observed option that does not exist
"""


class StockTest(unittest.TestCase):
    def test_createStock(self):
        bbas3 = Stock("Banco do Brasil", "BBAS3")
        self.assertEqual("Banco do Brasil", bbas3.name)
        self.assertEqual("BBAS3", bbas3.symbol)

    def test_definePrice(self):
        petr4 = Stock("Petrobrás", "PETR4")
        petr4.price = 8.65
        self.assertEqual(8.65, petr4.price)

    def test_defineVolatility(self):
        bbdc4 = Stock("Bradesco", "BBDC4")
        bbdc4.volatility = 78.56
        self.assertEqual(78.56, bbdc4.volatility)

    def test_observeOption(self):
        grnd3 = Stock("Grendene", "GRND3")
        grnd3.observeOption("GRNDQ20", 20.0, datetime.date(2016, 5, 29))
        self.assertEqual(20.0, grnd3.observedOptions["GRNDQ20"].strike)
        self.assertEqual(datetime.date(2016, 5, 29),
                         grnd3.observedOptions["GRNDQ20"].expirationDate)

    def test_buyObservedOption(self):
        elet6 = Stock("Eletrobrás", "ELET6")
        elet6.observeOption("ELETI12", 11.8, datetime.date(2016, 8, 22))
        elet6.buyOption("ELETI12", 0.82)
        # Option must leave observedOptions dict and go to boughtOptions one
        self.assertEqual({}, elet6.observedOptions)
        self.assertEqual(0.82, elet6.boughtOptions["ELETI12"].price)
        self.assertEqual(11.8, elet6.boughtOptions["ELETI12"].strike)
        self.assertEqual(datetime.date(2016, 8, 22),
                         elet6.boughtOptions["ELETI12"].expirationDate)

    def test_buyUnobservedOption(self):
        cvcb3 = Stock("CVC", "CVCB3")
        cvcb3.buyOption("CVCBV19", 0.43, 10.34, datetime.date(2016, 10, 19))
        # No options must exist in observedOptions dict
        self.assertEqual({}, cvcb3.observedOptions)
        self.assertEqual(0.43, cvcb3.boughtOptions["CVCBV19"].price)
        self.assertEqual(10.34, cvcb3.boughtOptions["CVCBV19"].strike)
        self.assertEqual(datetime.date(2016, 10, 19),
                         cvcb3.boughtOptions["CVCBV19"].expirationDate)
