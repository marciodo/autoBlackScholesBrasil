# coding: utf-8
import unittest
from blackscholes import database
from blackscholes.stock import Stock
import yaml

'''TODO:
        - Verify if we can save and load option dictionaries using yaml
'''


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
        ggbr3_dump = yaml.dump(ggbr3)
        # Create the same object from load
        ggbr3_fromLoad = yaml.load(ggbr3_dump)

        self.assertEqual(ggbr3.name, ggbr3_fromLoad.name)
        self.assertEqual(ggbr3.symbol, ggbr3_fromLoad.symbol)
        self.assertEqual(ggbr3.price, ggbr3_fromLoad.price)
        self.assertEqual(ggbr3.volatility, ggbr3_fromLoad.volatility)

if __name__ == '__main__':
    unittest.main()
