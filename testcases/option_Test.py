import unittest
import datetime
from blacksholes.option import Option

""" TODO:
    - Regular expression in option symbol
"""


class OptionTest(unittest.TestCase):

    def test_createOptionWithoutPrice(self):
        option = Option('abc', 12.3, datetime.date(2016, 4, 28))
        self.assertEqual(option.symbol, 'abc')
        self.assertEqual(option.strike, 12.3)
        self.assertEqual(option.expirationDate,
                         datetime.date(2016, 4, 28))
        self.assertEqual(option.price, 0)

    def test_createOptionWithPrice(self):
        option = Option('def', 15.2, datetime.date(2015, 3, 15), 0.75)
        self.assertEqual(option.symbol, 'def')
        self.assertEqual(option.strike, 15.2)
        self.assertEqual(option.expirationDate,
                         datetime.date(2015, 3, 15))
        self.assertEqual(option.price, 0.75)

    def test_invalidArgumentsWhenCreating(self):
        self.assertRaises(TypeError, Option, 15, 39.2,
                          datetime.date(2017, 2, 12))
        self.assertRaises(TypeError, Option, "BBASE74", "bla",
                          datetime.date(2000, 1, 9))
        self.assertRaises(TypeError, Option, "BBASE74", 12.3, 1234)
        self.assertRaises(TypeError, Option, "BBASE74", 2.45,
                          datetime.date(2000, 1, 9), True)

if __name__ == '__main__':
    unittest.main()
