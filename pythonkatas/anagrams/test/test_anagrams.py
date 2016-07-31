import unittest
from src.anagrams import *

class testAnagrams(unittest.TestCase):

    def test_stripSpacesAndPunctuation(self):
        testlist = ["pin kin", "pumpkin's", "Frienmd"]
        expected = ["pinkin", "pumpkins", "frienmd"]
        actual = [parseWords(i) for i in testlist]
        self.assertEqual(expected, actual)

    def test_FindAnagramsInList(self):
        expected = 1
        testlist = ["kinship", "pink ish", "pink'ish", "onkish", "shkinship"]
        actual = len(findAnagramsInList(testlist))
        self.assertEqual(expected, actual)


    def test_FindAnagramsInFile(self):
        expected = 7
        wordlist = load_words("wordlist.txt")
        actual = len(findAnagramsInList(wordlist))
        self.assertEqual(expected, actual)
