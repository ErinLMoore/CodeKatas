import unittest
from src.anagrams import *

class testAnagrams(unittest.TestCase):

    def test_FindAnagramsInList(self):
        expected = 1
        testlist = ["kinship", "pinkish", "piknish", "onkish", "shkinship"]
        testlist = [parseWords(i)for i in testlist]
        actual = len(findAnagramsInList(testlist))
        self.assertEqual(expected, actual)


    def test_FindAnagramsInFile(self):
        expected = 20683
        wordlist = load_words("wordlist.txt")
        actual = len(findAnagramsInList(wordlist))
        self.assertEqual(expected, actual)
