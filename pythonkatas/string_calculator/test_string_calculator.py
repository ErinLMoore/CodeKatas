import unittest
from string_calculator import add

class testStringCalculator(unittest.TestCase):

    def test_returns_zero_for_an_empty_string(self):
        expected = "0"
        actual = add("")
        self.assertEqual(expected, actual)

    def test_if_given_a_two_returns_a_two(self):
        expected = "2"
        actual = add("2")
        self.assertEqual(expected, actual)
