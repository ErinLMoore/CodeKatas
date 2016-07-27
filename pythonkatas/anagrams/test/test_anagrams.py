import unittest
from src.anagrams import findAnagrams

class testAnagrams(unittest.TestCase):

    def test_findAnagrams(self):
        expected = 1
        actual = findAnagrams()
        self.assertEqual(expected, actual)
