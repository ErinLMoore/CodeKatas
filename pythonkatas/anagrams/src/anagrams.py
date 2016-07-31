
def parseWords(word):
    returnword = word.lower()
    returnword = returnword.replace(" ", "")
    returnword = returnword.replace("'", "")
    return returnword

def load_words(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip()

def findAnagramsInList(wordlist):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    returnlist = []
    for word in wordlist:
        key = "".join(sorted(parseWords(word)))
        anagram_dict[key].append(word)
    returnlist = [anagrams for key, anagrams in anagram_dict.iteritems() if len(anagrams) > 1]
    return returnlist
