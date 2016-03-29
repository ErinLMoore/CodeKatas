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
    def test_returns_for_multiples_of_10(self):
        self.assertEqual('XX', ArabicToRoman.return_value(self.atr, 20))
        self.assertEqual('XXX', ArabicToRoman.return_value(self.atr, 30))
    def test_returns_for_multiples_of_1(self):
        self.assertEqual('II', ArabicToRoman.return_value(self.atr,2))
        self.assertEqual('III', ArabicToRoman.return_value(self.atr,3))
    def test_returns_for_500(self):
        self.assertEqual('D', ArabicToRoman.return_value(self.atr,500))
    def test_returns_for_50(self):
        self.assertEqual('L', ArabicToRoman.return_value(self.atr,50))
    def test_returns_for_5(self):
        self.assertEqual('V', ArabicToRoman.return_value(self.atr,5))
