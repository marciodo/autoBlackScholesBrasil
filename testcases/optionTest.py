import unittest
import datetime
from blacksholes.option import Option

""" TODO:
    - Regular expression in option symbol
"""


class OptionTest(unittest.TestCase):

    def test_createOptionWithoutPrice(self):
        self.option = Option('abc', 12.3, datetime.date(2016, 4, 28))
        self.assertEqual(self.option.symbol, 'abc')
        self.assertEqual(self.option.strike, 12.3)
        self.assertEqual(self.option.expirationDate,
                         datetime.date(2016, 4, 28))
        self.assertEqual(self.option.price, 0)

if __name__ == '__main__':
    unittest.main()
