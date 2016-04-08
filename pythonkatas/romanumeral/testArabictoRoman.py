# -*- coding: utf-8 -*-
import unittest
from romannumeral import ArabicToRoman

class testArabictoRoman(unittest.TestCase):

    def setUp(self):
        self.atr = ArabicToRoman()

    def test_returns_for_multiples_of_1000(self):
        input = 2000
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('MM', result)
    def test_returns_for_multiples_of_100(self):
        input = 200
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('CC', result)
    def test_returns_for_multiples_of_10(self):
        input = 30
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('XXX', result)
    def test_returns_for_multiples_of_1(self):
        input = 2
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('II', result)
    def test_returns_for_500(self):
        input = 500
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('D', result)
    def test_returns_for_50(self):
        input = 50
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('L', result)
    def test_returns_for_5(self):
        input = 5
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('V', result)
    def test_returns_for_2777_to_put_it_all_together(self):
        input = 2777
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('MMDCCLXXVII', result)
    def test_returns_for_900(self):
        input = 900
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('CM', result)
    def test_returns_for_400(self):
        input = 400
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('CD', result)
    def test_returns_for_90(self):
        input = 90
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('XC', result)
    def test_returns_for_40(self):
        input = 40
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('XL', result)
    def test_returns_for_9(self):
        input = 9
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('IX', result)
    def test_returns_for_4(self):
        input = 4
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('IV', result)
    def test_return_for_3999_to_put_it_all_together(self):
        input =  3999
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('MMMCMXCIX', result)
    def test_return_for_5001(self):
        input = 5001
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('ↁI', result)
    def test_return_for_39440(self):
        input = 39440
        result = (ArabicToRoman.return_value(self.atr, input))
        self.assertEqual('ↂↂↂMↂCDXL', result)
