import unittest
from src.anagrams import compareWords

class testAnagrams(unittest.TestCase):

    def test_AnagramsAreCompared(self):
        expected = True
        actual = compareWords("kinship", "pinkish")
        self.assertEqual(expected, actual)

        expected = False
        actual = compareWords("kinship", "ponkish")
        self.assertEqual(expected, actual)
