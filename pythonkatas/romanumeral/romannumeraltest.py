import unittest
from romannumeral import ArabicToRoman

class testRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returnsIifgiven1(self):
        self.assertEqual('I', ArabicToRoman.return_value(self.atr, 1))
