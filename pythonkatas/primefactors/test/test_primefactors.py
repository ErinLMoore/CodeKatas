import unittest
from src.primefactors import primeFactors

class testPrimeFactors(unittest.TestCase):

    def test_returns_a_one_if_given_one(self):
        expected = [1]
        actual = primeFactors(1)
        self.assertEqual(expected, actual)

    def test_returns_a_two_if_given_two(self):
        expected = [1,2]
        actual = primeFactors(2)
        self.assertEqual(expected, actual)

    def test_returns_a_two_if_given_four(self):
        expected = [1,2,4]
        actual = primeFactors(4)
        self.assertEqual(expected, actual)
