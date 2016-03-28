import unittest
from romannumeral import ArabicToRoman

class testArabictoRoman(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returns_for_multiples_of_1000(self):
        self.assertEqual('MM', ArabicToRoman.return_value(self.atr, 2000))
        self.assertEqual('MMM', ArabicToRoman.return_value(self.atr, 3000))
    def test_returns_for_multiples_of_100(self):
        self.assertEqual('CC', ArabicToRoman.return_value(self.atr, 200))
        self.assertEqual('CCC', ArabicToRoman.return_value(self.atr, 300))
