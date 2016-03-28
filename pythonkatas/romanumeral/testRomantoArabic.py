import unittest
from romannumeral import RomantoArabic

class testRomantoArabic(unittest.TestCase):

    def setUp(self):
        self.rta = RomantoArabic()

    def test_returns_1_through_3(self):
        self.assertEqual(1, RomantoArabic.return_value(self.rta, 'I'))
        self.assertEqual(3, RomantoArabic.return_value(self.rta, 'III'))

    def test_returns_4_for_IV(self):
        self.assertEqual(4, RomantoArabic.return_value(self.rta, 'IV'))
