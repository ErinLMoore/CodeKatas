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
