import unittest
from romannumeral import ArabicToRoman

class testRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returnsI_through_III_for_1_through_3(self):
        self.assertEqual('I', ArabicToRoman.return_value(self.atr, 1))
        self.assertEqual('III', ArabicToRoman.return_value(self.atr, 3))
