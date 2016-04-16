import unittest
import datetime
from blacksholes.option import Option
from blacksholes.option import optionType


class OptionTest(unittest.TestCase):

    def test_createOptionWithoutPrice(self):
        option = Option('PETRD78', 12.3, datetime.date(2016, 4, 28))
        self.assertEqual(option.symbol, 'PETRD78')
        self.assertEqual(option.strike, 12.3)
        self.assertEqual(option.expirationDate,
                         datetime.date(2016, 4, 28))
        self.assertEqual(option.price, 0)
        self.assertEqual(option.type, optionType.CALL)

    def test_createOptionWithPrice(self):
        option = Option('BBDCo23', 15.2, datetime.date(2015, 3, 15), 0.75)
        self.assertEqual(option.symbol, 'BBDCo23')
        self.assertEqual(option.strike, 15.2)
        self.assertEqual(option.expirationDate,
                         datetime.date(2015, 3, 15))
        self.assertEqual(option.price, 0.75)
        self.assertEqual(option.type, optionType.PUT)

    def test_invalidArgumentsWhenCreating(self):
        self.assertRaises(TypeError, Option, 15, 39.2,
                          datetime.date(2017, 2, 12))
        self.assertRaises(TypeError, Option, "BBASE74", "bla",
                          datetime.date(2000, 1, 9))
        self.assertRaises(TypeError, Option, "BBASE74", 12.3, 1234)
        self.assertRaises(TypeError, Option, "BBASE74", 2.45,
                          datetime.date(2000, 1, 9), True)

    def test_invalidOptionNameWhenCreating(self):
        self.assertRaises(ValueError, Option, "ble", 32.5,
                          datetime.date(2021, 4, 30))


if __name__ == '__main__':
    unittest.main()
