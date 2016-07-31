import unittest
from src.anagrams import *

class testAnagrams(unittest.TestCase):

    def test_AnagramsAreCompared(self):
        expected = True
        actual = compareWords("kinship", "pinkish")
        self.assertEqual(expected, actual)

        expected = False
        actual = compareWords("kinship", "ponkish")
        self.assertEqual(expected, actual)

    def test_AnagramFoundInList(self):
        expected = 1
        actual = len(findWordsInList("kinship",["pinkish", "ponkish"]))
        self.assertEqual(expected, actual)
