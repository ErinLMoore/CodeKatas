def compareWords(word1, word2):
    word1 =''.join(sorted(word1))
    word2 =''.join(sorted(word2))
    return word1 == word2

def findWordsInList(searchword, searchlist):
    returnlist = []
    for i in searchlist:
        if compareWords(searchword, i) == True:
            returnlist.append(i)
    return returnlist
