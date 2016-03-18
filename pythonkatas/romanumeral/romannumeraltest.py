import unittest
from romannumeral import ArabicToRoman

class testRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returnsI_through_III_for_1_through_3(self):
        self.assertEqual('I', ArabicToRoman.return_value(self.atr, 1))
        self.assertEqual('III', ArabicToRoman.return_value(self.atr, 3))

    def test_returns_properly_for_non_repeatables(self):
        self.assertEqual('IV', ArabicToRoman.return_value(self.atr, 4))
        self.assertEqual('V', ArabicToRoman.return_value(self.atr, 5))
        self.assertEqual('IX', ArabicToRoman.return_value(self.atr, 9))
        self.assertEqual('XL', ArabicToRoman.return_value(self.atr, 40))

    def test_returnsVI_VIII_for_six_through_8(self):
        self.assertEqual('VI', ArabicToRoman.return_value(self.atr, 6))
        self.assertEqual('VIII', ArabicToRoman.return_value(self.atr, 8))

    def test_returns_properly_for_10_through_19(self):
        self.assertEqual('X', ArabicToRoman.return_value(self.atr, 10))
        self.assertEqual('XIII', ArabicToRoman.return_value(self.atr, 13))
        self.assertEqual('XIV', ArabicToRoman.return_value(self.atr, 14))
        self.assertEqual('XVI', ArabicToRoman.return_value(self.atr, 16))
        self.assertEqual('XIX', ArabicToRoman.return_value(self.atr, 19))

    def test_returns_for_multiples_of_10(self):
        self.assertEqual('XX', ArabicToRoman.return_value(self.atr, 20))
        self.assertEqual('XXX', ArabicToRoman.return_value(self.atr, 30))

    def test_returns_for_20_through_40(self):
        self.assertEqual('XXII', ArabicToRoman.return_value(self.atr, 22))
        self.assertEqual('XXIV', ArabicToRoman.return_value(self.atr, 24))
        self.assertEqual('XXXIII', ArabicToRoman.return_value(self.atr, 33))
        self.assertEqual('XXXIX', ArabicToRoman.return_value(self.atr, 39))

    def test_returns_for_40_through_59(self):
        self.assertEqual('XLIV', ArabicToRoman.return_value(self.atr, 44))
        self.assertEqual('XLIX', ArabicToRoman.return_value(self.atr, 49))
        self.assertEqual('LII', ArabicToRoman.return_value(self.atr, 52))
        self.assertEqual('LVIII', ArabicToRoman.return_value(self.atr, 58))

    def test_returns_for_60_through_89(self):
        self.assertEqual('LXIII', ArabicToRoman.return_value(self.atr, 63))
        self.assertEqual('LXIX', ArabicToRoman.return_value(self.atr, 69))
        self.assertEqual('LXXVII', ArabicToRoman.return_value(self.atr, 77))
        self.assertEqual('LXXXI', ArabicToRoman.return_value(self.atr, 81))

    def test_returns_for_90_through_99(self):
        self.assertEqual('XCIII', ArabicToRoman.return_value(self.atr, 93))
        self.assertEqual('XCIX', ArabicToRoman.return_value(self.atr, 99))
