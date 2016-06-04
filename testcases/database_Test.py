# coding: utf-8
import unittest
from blackscholes import database
from blackscholes.stock import Stock
from blackscholes.option import Option
from numpy import datetime64
import yaml


class BlachscholesTest(unittest.TestCase):

    def test_saveStock_noPrice_noVol_noOption(self):
        ggbr3 = Stock('Gerdau', 'GGBR3')
        database.saveStock(ggbr3)

    def test_saveObjectAsYaml(self):
        # Test of yaml generating and loading the same object
        # to see its working way
        ggbr3 = Stock('Gerdau', 'GGBR3')
        ggbr3.price = 4.01
        ggbr3.volatility = 78.6

        ggbr3.observeOption('GGBRM4', 3.5, datetime64('2017-01-20'))
        ggbr3.buyOption('GGBRA48', 0.27, 4.8, datetime64('2018-01-20'))

        yaml.add_representer(datetime64, datetime64Representer)
        yaml.add_constructor(u'datetime64', datetime64Constructor)
        ggbr3_dump = yaml.dump(ggbr3)
        # Create the same object from load
        ggbr3_fromLoad = yaml.load(ggbr3_dump)

        # Test if dumped stock is equal loaded stock
        self.assertEqual(ggbr3.name, ggbr3_fromLoad.name)
        self.assertEqual(ggbr3.symbol, ggbr3_fromLoad.symbol)
        self.assertEqual(ggbr3.price, ggbr3_fromLoad.price)
        self.assertEqual(ggbr3.volatility, ggbr3_fromLoad.volatility)
        # Test if dumped observedOptions is equal loaded observedOptions
        self.assertEqual(ggbr3.observedOptions['GGBRM4'].symbol,
                         ggbr3_fromLoad.observedOptions['GGBRM4'].symbol)
        self.assertEqual(ggbr3.observedOptions['GGBRM4'].strike,
                         ggbr3_fromLoad.observedOptions['GGBRM4'].strike)
        self.assertEqual(ggbr3.observedOptions['GGBRM4'].expirationDate,
                         ggbr3_fromLoad.observedOptions['GGBRM4'].
                         expirationDate)
        self.assertEqual(ggbr3.observedOptions['GGBRM4'].type,
                         ggbr3_fromLoad.observedOptions['GGBRM4'].type)
        # Test if dumped boughtOptions is equal loaded boughtOptions
        self.assertEqual(ggbr3.boughtOptions['GGBRA48'].symbol,
                         ggbr3_fromLoad.boughtOptions['GGBRA48'].symbol)
        self.assertEqual(ggbr3.boughtOptions['GGBRA48'].strike,
                         ggbr3_fromLoad.boughtOptions['GGBRA48'].strike)
        self.assertEqual(ggbr3.boughtOptions['GGBRA48'].expirationDate,
                         ggbr3_fromLoad.boughtOptions['GGBRA48'].
                         expirationDate)
        self.assertEqual(ggbr3.boughtOptions['GGBRA48'].type,
                         ggbr3_fromLoad.boughtOptions['GGBRA48'].type)


def datetime64Representer(dumper, data):
    return dumper.represent_scalar(u'datetime64', str(data))


def datetime64Constructor(loader, node):
    value = loader.construct_scalar(node)
    return datetime64(value)


if __name__ == '__main__':
    unittest.main()
