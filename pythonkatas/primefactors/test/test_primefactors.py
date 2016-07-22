import unittest
import src.primefactors

class testPrimeFactors(unittest.TestCase):

    def test_returns_one_if_given_one(self):
        expected = 1
        actual = primefactors.primeFactors(1)
        self.assertEqual(expected, actual)
