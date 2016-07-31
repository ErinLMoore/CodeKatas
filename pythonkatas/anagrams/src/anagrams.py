def compareWords(word1, word2):
    word1 =''.join(sorted(word1))
    word2 =''.join(sorted(word2))
    return word1 == word2

def findWordsInList(searchword, searchlist):
    returnlist = [i for i in searchlist if compareWords(searchword, i) == True]
    return returnlist

def checkWordLength(searchword, searchlist):
    returnlist = [i for i in searchlist if len(i) == len(searchword)]
    return returnlist

def parseWordsInList(wordlist):
    returnlist = [i.lower() for i in wordlist]
    returnlist = [i.replace(" ", "") for i in returnlist]
    returnlist = [i.replace("'", "") for i in returnlist]

    return returnlist
