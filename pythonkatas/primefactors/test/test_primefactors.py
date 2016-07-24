import unittest
from src.primefactors import primeFactors

class testPrimeFactors(unittest.TestCase):

    def test_returns_one_if_given_one(self):
        expected = 1
        actual = primeFactors(1)
        self.assertEqual(expected, actual)
