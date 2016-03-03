import unittest
from fizzbuzz import Fizzbuzz

class testFizzbuzz(unittest.TestCase):

    def setUp(self):
        # init fizzbuzz class
        self.fizzbuzz = Fizzbuzz()

    def test_returns_one_if_given_one(self):
        self.assertEqual(1, Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 1))

    def test_returns_two_if_given_two(self):
        self.assertEqual(2, Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 2))
