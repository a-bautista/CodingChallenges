'''
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
    sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
    shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

    This is an undirected graph structure.

    Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

    Hit -> Hot -> Dot -> Dog -> Cog

    First, you need to start by creating a dictionary with the index of the intermediate word 
    and a list of possible
    words related to that index

    hit         --> 2
    dot hot lot --> 3
    dog log     --> 4
    cog         --> 5

'''

from collections import deque
from string import ascii_letters
def solve_ladder(beginWord, endWord, wordList):

    queue = deque()
    setOfWords = set(wordList)
    # the question is how many words you will be transformed that are in the set of words to reach your target
    distance = 1
    queue.append(beginWord)

    while queue:
        currentWordsInLevel = len(queue)
        distance +=1
        
        # for the current words in the queue
        for _ in range(currentWordsInLevel):
            currentWord = queue.popleft()
            currentLenOfWord = len(currentWord)
            
            # for each letter of the current word
            for i in range(currentLenOfWord):
                # for each char in the set of ascii letters just create the new word
                for char in ascii_letters:
                    # hit
                    # *  then a then it = ait
                    # *  then b then it = bit
                    # ...
                    # hit
                    # h * then a then t = hat
                    # h * then b then t = hbt
                    newWord = currentWord[:i] + char + currentWord[i+1:]

                    if newWord == endWord:
                        return distance
                    if newWord not in setOfWords:
                        continue
                    if newWord in setOfWords:
                        queue.append(newWord)
                        setOfWords.remove(newWord)
    return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = solve_ladder(beginWord, endWord, wordList)
    print(res)

main()