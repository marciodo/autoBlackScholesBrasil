# coding: utf-8
import unittest
from numpy import datetime64
from blackscholes.stock import Stock
from blackscholes.stock import ObserveError
from blackscholes.stock import BuyError


class StockTest(unittest.TestCase):
    def test_createStock(self):
        bbas3 = Stock('Banco do Brasil', 'BBAS3')
        self.assertEqual('Banco do Brasil', bbas3.name)
        self.assertEqual('BBAS3', bbas3.symbol)

    def test_definePrice(self):
        petr4 = Stock('Petrobrás', 'PETR4')
        petr4.price = 8.65
        self.assertEqual(8.65, petr4.price)

    def test_defineVolatility(self):
        bbdc4 = Stock('Bradesco', 'BBDC4')
        bbdc4.volatility = 78.56
        self.assertEqual(78.56, bbdc4.volatility)

    def test_observeOption(self):
        grnd3 = Stock('Grendene', 'GRND3')
        grnd3.observeOption('GRNDQ20', 20.0, datetime64('2016-05-29'))
        self.assertEqual(20.0, grnd3.observedOptions['GRNDQ20'].strike)
        self.assertEqual(datetime64('2016-05-29'),
                         grnd3.observedOptions['GRNDQ20'].expirationDate)

    def test_buyObservedOption(self):
        elet6 = Stock('Eletrobrás', 'ELET6')
        elet6.observeOption('ELETI12', 11.8, datetime64('2016-08-22'))
        elet6.buyOption('ELETI12', 0.82)
        # Option must leave observedOptions dict and go to boughtOptions one
        self.assertEqual({}, elet6.observedOptions)
        self.assertEqual(0.82, elet6.boughtOptions['ELETI12'].price)
        self.assertEqual(11.8, elet6.boughtOptions['ELETI12'].strike)
        self.assertEqual(datetime64('2016-08-22'),
                         elet6.boughtOptions['ELETI12'].expirationDate)

    def test_buyUnobservedOption(self):
        cvcb3 = Stock('CVC', 'CVCB3')
        cvcb3.buyOption('CVCBV19', 0.43, 10.34, datetime64('2016-10-19'))
        # No options must exist in observedOptions dict
        self.assertEqual({}, cvcb3.observedOptions)
        self.assertEqual(0.43, cvcb3.boughtOptions['CVCBV19'].price)
        self.assertEqual(10.34, cvcb3.boughtOptions['CVCBV19'].strike)
        self.assertEqual(datetime64('2016-10-19'),
                         cvcb3.boughtOptions['CVCBV19'].expirationDate)

    def test_observeAnAlreadyObservedOption(self):
        tecn3 = Stock('Technos', 'TECN3')
        tecn3.observeOption('TECNN45', 4.5, datetime64('2013-12-23'))
        self.assertRaises(ObserveError, tecn3.observeOption, 'TECNN45', 4.7,
                          datetime64('2015-12-21'))

    def test_buyAnAlreadyObservedOptionLikeItWasNot(self):
        bsrs6 = Stock('Banco do Rio Grande do Sul', 'BSRS6')
        bsrs6.observeOption('BRSRX12', 12.0, datetime64('2020-12-20'))
        self.assertRaises(BuyError, bsrs6.buyOption, 'BRSRX12', 0.32, 11.8,
                          datetime64('2017-12-19'))

    def test_buyAnUnobservedOptionLikeItWasObserved(self):
        eter3 = Stock('Eternit', 'ETER3')
        self.assertRaises(BuyError, eter3.buyOption, 'ETERA89', 0.67)

if __name__ == '__main__':
    unittest.main()
