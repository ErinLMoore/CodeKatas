import unittest
from romannumeral import ArabicToRoman

class testRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returnsI_through_III_for_1_through_3(self):
        self.assertEqual('I', ArabicToRoman.return_value(self.atr, 1))
        self.assertEqual('III', ArabicToRoman.return_value(self.atr, 3))

    def test_returnsIV_for_four(self):
        self.assertEqual('IV', ArabicToRoman.return_value(self.atr, 4))

    def test_returnsV_for_five(self):
        self.assertEqual('V', ArabicToRoman.return_value(self.atr, 5))

    def test_returnsVI_VIII_for_six_through_8(self):
        self.assertEqual('VI', ArabicToRoman.return_value(self.atr, 6))
        self.assertEqual('VIII', ArabicToRoman.return_value(self.atr, 8))

    def test_returnsIX_for_9(self):
        self.assertEqual('IX', ArabicToRoman.return_value(self.atr, 9))

    def test_returns_properly_for_X_through_XIX(self):
        self.assertEqual('X', ArabicToRoman.return_value(self.atr, 10))
        self.assertEqual('XIII', ArabicToRoman.return_value(self.atr, 13))
        self.assertEqual('XIV', ArabicToRoman.return_value(self.atr, 14))
        self.assertEqual('XVI', ArabicToRoman.return_value(self.atr, 16))
        self.assertEqual('XIX', ArabicToRoman.return_value(self.atr, 19))

    def test_returns_for_multiples_of_10(self):
        self.assertEqual('XX', ArabicToRoman.return_value(self.atr, 20))
        self.assertEqual('XXX', ArabicToRoman.return_value(self.atr, 30))
