# coding: utf-8
import unittest
from blackscholes import config
from blackscholes.stock import Stock
from blackscholes.option import Option
from blackscholes import database
from numpy import datetime64
import yaml
import os

''' TODO:
- save many stocks to file
'''


class BlachscholesTest(unittest.TestCase):
    def setUp(self):
        self.testPath = os.path.expanduser('~') + os.sep
        self.testFile = os.path.join(os.sep, self.testPath, config.dbFilename)

    def test_createStockFile(self):
        ggbr3 = Stock('Gerdau', 'GGBR3')
        database.saveStock(ggbr3, self.testPath)
        self.assertTrue(os.path.exists(self.testFile))
        os.remove(self.testFile)

    def test_saveStock_noPrice_noVol_noOption(self):
        fesa4 = Stock('Ferbasa', 'FESA4')
        database.saveStock(fesa4, self.testPath)

        stream = file(self.testFile, 'r')
        fesa4_fromFile = yaml.load(stream)
        self.assertEqual(fesa4.name, fesa4_fromFile.name)
        self.assertEqual(fesa4.symbol, fesa4_fromFile.symbol)
        self.assertEqual(fesa4.price, fesa4_fromFile.price)
        self.assertEqual(fesa4.volatility, fesa4_fromFile.volatility)
        # Empty option dictionaries
        self.assertEqual(fesa4.observedOptions, fesa4_fromFile.observedOptions)
        self.assertEqual(fesa4.boughtOptions, fesa4_fromFile.boughtOptions)

        os.remove(self.testFile)

    def test_saveStock_noOption(self):
        suzb4 = Stock('Suzano', 'SUZB4')
        suzb4.price = 12.43
        suzb4.volatility = 34.54
        database.saveStock(suzb4, self.testPath)

        stream = file(self.testFile, 'r')
        suzb4_fromFile = yaml.load(stream)
        self.assertEqual(suzb4.name, suzb4_fromFile.name)
        self.assertEqual(suzb4.symbol, suzb4_fromFile.symbol)
        self.assertEqual(suzb4.price, suzb4_fromFile.price)
        self.assertEqual(suzb4.volatility, suzb4_fromFile.volatility)
        # Empty option dictionaries
        self.assertEqual(suzb4.observedOptions, suzb4_fromFile.observedOptions)
        self.assertEqual(suzb4.boughtOptions, suzb4_fromFile.boughtOptions)

        os.remove(self.testFile)

    def test_saveStock_2ObservedOptions(self):
        card3 = Stock('CSU Cardsystem', 'CARD3')
        card3.price = 4.57
        card3.volatility = 50.23
        card3.observeOption('CARDL50', 5.0, datetime64('2016-12-16'))
        card3.observeOption('CARDL52', 5.2, datetime64('2016-12-16'))
        database.saveStock(card3, self.testPath)

        stream = file(self.testFile, 'r')
        card3_fromFile = yaml.load(stream)
        self.assertEqual(card3.name, card3_fromFile.name)
        self.assertEqual(card3.symbol, card3_fromFile.symbol)
        self.assertEqual(card3.price, card3_fromFile.price)
        self.assertEqual(card3.volatility, card3_fromFile.volatility)

        # Evaluate each option data
        cardl50 = card3.observedOptions['CARDL50']
        cardl50_fromFile = card3_fromFile.observedOptions['CARDL50']
        self.assertEqual(cardl50.symbol, cardl50_fromFile.symbol)
        self.assertEqual(cardl50.strike, cardl50_fromFile.strike)
        self.assertEqual(cardl50.expirationDate,
                         cardl50_fromFile.expirationDate)
        self.assertEqual(cardl50.type, cardl50_fromFile.type)

        cardl52 = card3.observedOptions['CARDL52']
        cardl52_fromFile = card3_fromFile.observedOptions['CARDL52']
        self.assertEqual(cardl52.symbol, cardl52_fromFile.symbol)
        self.assertEqual(cardl52.strike, cardl52_fromFile.strike)
        self.assertEqual(cardl52.expirationDate,
                         cardl52_fromFile.expirationDate)
        self.assertEqual(cardl52.type, cardl52_fromFile.type)

        os.remove(self.testFile)

    def test_saveStock_2BoughtOptions(self):
        abcb3 = Stock('ABC Banco', 'ABCB3')
        abcb3.price = 3.76
        abcb3.volatility = 84.24
        abcb3.buyOption('ABCBR6', 0.23, 6.0, datetime64('2016-06-18'))
        abcb3.buyOption('ABCBR65', 0.12, 6.5, datetime64('2016-06-18'))
        database.saveStock(abcb3, self.testPath)

        stream = file(self.testFile, 'r')
        abcb3_fromFile = yaml.load(stream)
        self.assertEqual(abcb3.name, abcb3_fromFile.name)
        self.assertEqual(abcb3.symbol, abcb3_fromFile.symbol)
        self.assertEqual(abcb3.price, abcb3_fromFile.price)
        self.assertEqual(abcb3.volatility, abcb3_fromFile.volatility)

        # Evaluate each option data
        abcbr6 = abcb3.boughtOptions['ABCBR6']
        abcbr6_fromFile = abcb3_fromFile.boughtOptions['ABCBR6']
        self.assertEqual(abcbr6.symbol, abcbr6_fromFile.symbol)
        self.assertEqual(abcbr6.strike, abcbr6_fromFile.strike)
        self.assertEqual(abcbr6.expirationDate,
                         abcbr6_fromFile.expirationDate)
        self.assertEqual(abcbr6.type, abcbr6_fromFile.type)
        self.assertEqual(abcbr6.price, abcbr6_fromFile.price)

        abcbr65 = abcb3.boughtOptions['ABCBR65']
        abcbr65_fromFile = abcb3_fromFile.boughtOptions['ABCBR65']
        self.assertEqual(abcbr65.symbol, abcbr65_fromFile.symbol)
        self.assertEqual(abcbr65.strike, abcbr65_fromFile.strike)
        self.assertEqual(abcbr65.expirationDate,
                         abcbr65_fromFile.expirationDate)
        self.assertEqual(abcbr65.type, abcbr65_fromFile.type)
        self.assertEqual(abcbr65.price, abcbr65_fromFile.price)

        os.remove(self.testFile)

    def test_save2Stocks(self):
        eter3 = Stock('Eternit', 'ETER3')
        eter3.price = 6.23
        eter3.volatility = 90.43

        brpr3 = Stock('BR Properties', 'BRPR3')
        brpr3.price = 10.32
        brpr3.volatility = 21.43

        database.saveStock(eter3, '')
        database.saveStock(brpr3, '')

        #for data in yaml.load_all(config.dbFilename):
        #    print(data)

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
        ggbrm4 = ggbr3.observedOptions['GGBRM4']
        ggbrm4_fromLoad = ggbr3_fromLoad.observedOptions['GGBRM4']
        self.assertEqual(ggbrm4.symbol, ggbrm4.symbol)
        self.assertEqual(ggbrm4.strike, ggbrm4_fromLoad.strike)
        self.assertEqual(ggbrm4.expirationDate,
                         ggbrm4_fromLoad.expirationDate)
        self.assertEqual(ggbrm4.type, ggbrm4_fromLoad.type)
        # Test if dumped boughtOptions is equal loaded boughtOptions
        ggbra48 = ggbr3.boughtOptions['GGBRA48']
        ggbra48_fromLoad = ggbr3_fromLoad.boughtOptions['GGBRA48']
        self.assertEqual(ggbra48.symbol, ggbra48_fromLoad.symbol)
        self.assertEqual(ggbra48.strike, ggbra48_fromLoad.strike)
        self.assertEqual(ggbra48.expirationDate,
                         ggbra48_fromLoad.expirationDate)
        self.assertEqual(ggbra48.type, ggbra48_fromLoad.type)
        self.assertEqual(ggbra48.price, ggbra48_fromLoad.price)


def datetime64Representer(dumper, data):
    return dumper.represent_scalar(u'datetime64', str(data))


def datetime64Constructor(loader, node):
    value = loader.construct_scalar(node)
    return datetime64(value)


if __name__ == '__main__':
    unittest.main()
