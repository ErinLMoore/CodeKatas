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

    def test_returns_buzz_if_given_three(self):
        self.assertEqual("Buzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 3))

    def test_returns_buzz_if_given_six(self):
        self.assertEqual("Buzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 6))

    def test_returns_fizz_if_given_five(self):
        self.assertEqual("Fizz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 5))

    def test_returns_fizz_if_given_ten(self):
        self.assertEqual("Fizz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 10))
