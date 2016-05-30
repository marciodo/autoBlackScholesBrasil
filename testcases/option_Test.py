import unittest
from numpy import datetime64
from blackscholes.option import Option
from blackscholes.option import optionType


class OptionTest(unittest.TestCase):

    def test_createOptionWithoutPrice(self):
        option = Option('PETRD78', 12.3, datetime64('2016-04-28'))
        self.assertEqual(option.symbol, 'PETRD78')
        self.assertEqual(option.strike, 12.3)
        self.assertEqual(option.expirationDate,
                         datetime64('2016-04-28'))
        self.assertEqual(option.price, 0)
        self.assertEqual(option.type, optionType.CALL)

    def test_createOptionWithPrice(self):
        option = Option('BBDCo2', 15.2, datetime64('2015-03-15'), 0.75)
        self.assertEqual(option.symbol, 'BBDCo2')
        self.assertEqual(option.strike, 15.2)
        self.assertEqual(option.expirationDate,
                         datetime64('2015-03-15'))
        self.assertEqual(option.price, 0.75)
        self.assertEqual(option.type, optionType.PUT)

    def test_invalidArgumentsWhenCreating(self):
        self.assertRaises(TypeError, Option, 15, 39.2,
                          datetime64('2017-02-12'))
        self.assertRaises(TypeError, Option, 'BBASE74', 'bla',
                          datetime64('2000-01-09'))
        self.assertRaises(TypeError, Option, 'BBASE74', 12.3, 1234)
        self.assertRaises(TypeError, Option, 'BBASE74', 2.45,
                          datetime64('2000-01-09'), True)

    def test_invalidOptionNameWhenCreating(self):
        self.assertRaises(ValueError, Option, 'ble', 32.5,
                          datetime64('2021-04-30'))


if __name__ == '__main__':
    unittest.main()
