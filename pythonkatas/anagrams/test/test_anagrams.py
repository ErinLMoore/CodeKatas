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

    def test_discardWordsOfWrongLength(self):
        expected = 1
        actual = len(checkWordLength("kinship",["pinkish", "onkish", "  kinship"]))
        self.assertEqual(expected, actual)

    def test_stripSpacesAndPunctuation(self):
        testlist = ["pin kin", "pumpkin's", "Frienmd"]
        expected = ["pinkin", "pumpkins", "frienmd"]
        actual = parseWordsInList(testlist)
        self.assertEqual(expected, actual)

    def test_integrationFindAnagramsInList(self):
        expected = 2
        testword = "kinship"
        testlist = ["pink ish", "pink'ish", "onkish", "shkinship"]
        testlist = parseWordsInList(testlist)
        testlist = checkWordLength(testword, testlist)
        actual = len(findWordsInList(testword, testlist))
        self.assertEqual(expected, actual)
