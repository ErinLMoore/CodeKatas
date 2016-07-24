import unittest
from src.primefactors import primeFactors

class testPrimeFactors(unittest.TestCase):

    def test_returns_one_if_given_one(self):
        expected = [1]
        actual = primeFactors(1)
        self.assertEqual(expected, actual)

    def test_returns_two_if_given_two(self):
        expected = [2]
        actual = primeFactors(2)
        self.assertEqual(expected, actual)

    def test_returns_eleven_if_given_eleven(self):
        expected = [11]
        actual = primeFactors(11)
        self.assertEqual(expected, actual)

    def test_returns_a_two_if_given_four(self):
        expected = [2,2]
        actual = primeFactors(4)
        self.assertEqual(expected, actual)

    def test_returns_a_two_two_five_given_twenty(self):
        expected = [2,2,5]
        actual = primeFactors(20)
        self.assertEqual(expected, actual)
