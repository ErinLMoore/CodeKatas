def load_words(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            yield line.rstrip()

def findAnagramsInList(wordlist):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for word in wordlist:
        key = "".join(sorted(word))
        anagram_dict[key].append(word)
    returnlist = [anagrams for key, anagrams in anagram_dict.iteritems() if len(anagrams) > 1]
    printAnagramsToFile(returnlist)
    return returnlist

def printAnagramsToFile(anagramlist):
    with open('anagrams.txt', mode='wt') as anagramfile:
        for line in anagramlist:
            for word in line:
                anagramfile.write(''.join(word) + ' ')
            anagramfile.write('\n')
