import unittest
from string_calculator import add

class testStringCalculator(unittest.TestCase):

    def test_returns_zero_for_an_empty_string(self):
        expected = "0"
        actual = add("")
        self.assertEqual(expected, actual)
