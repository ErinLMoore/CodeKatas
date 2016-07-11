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

    def test_if_given_a_four_returns_a_four(self):
        expected = "4"
        actual = add("4")
        self.assertEqual(expected, actual)

    def test_adds_one_and_one_and_returns_two(self):
        expected = "2"
        actual = add("1,1")
        self.assertEqual(expected,actual)

    def test_adds_two_strings_returns_sum(self):
        expected = "807"
        actual = add("747,60")
        self.assertEqual(expected,actual)

    def test_adds_three_strings_returns_sum(self):
        expected = "809"
        actual = add("747,60,2")
        self.assertEqual(expected,actual)

    def test_can_use_newlines_to_delimit(self):
        expected = "2"
        actual = add("1\n1")
        self.assertEqual(expected,actual)
