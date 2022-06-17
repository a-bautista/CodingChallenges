'''
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation 
    sequences from beginWord to endWord, or an empty list if no such sequence exists. 
    Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
    Example 1:

    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    Explanation: There are 2 shortest transformation sequences:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    "hit" -> "hot" -> "lot" -> "log" -> "cog"
'''
from string import ascii_letters
from collections import defaultdict
def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = defaultdict(list)
        for w in layer:
            if w == endWord: 
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in ascii_letters:
                        neww = w[:i]+c+w[i+1:]
                        if neww in wordList:
                            for j in layer[w]:
                                newlayer[neww]+=[j+[neww]]    
                            #newlayer[neww]+=[j+[neww] for j in layer[w]]

        wordList -= set(newlayer.keys())
        layer = newlayer
    
    return res

def main():

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = findLadders(beginWord, endWord, wordList)
    print(res)

main()