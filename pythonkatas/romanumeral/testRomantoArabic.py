import unittest
from romannumeral import RomantoArabic

class testRomantoArabic(unittest.TestCase):

    def setUp(self):
        self.rta = RomantoArabic()

    def test_returns_1_for_I(self):
        self.assertEqual(1, RomantoArabic.return_value(self.rta, 'I'))
