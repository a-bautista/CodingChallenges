"""
    This is an undirected graph structure.

    Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

    Hit -> Hot -> Dot -> Dog -> Cog

    First, you need to start by creating a dictionary with the index of the intermediate word and a list of possible
    words related to that index


    {'*ot': [],
    'h*t': [],
    'ho*': [],
    'd*t': [],
    'do*': ['dot', 'dog'],
    '*og': ['dog', 'log', 'cog'],
    'd*g': ['dog'],
    'l*t': ['lot'],
    'lo*': ['lot', 'log'],
    'l*g': ['log'],
    'c*g': ['cog'],
    'co*': ['cog'],
    '*it': [],
    'hi*': []})

"""


from collections import deque, defaultdict
from string import ascii_letters

def ladderLength(begin, end, word_list):
    words = set(word_list) # make a set because existence query is O(1) vs O(N) for list
    queue = deque()
    queue.append(begin)
    distance = 1

    while queue:
        n = len(queue)
        distance += 1
        for _ in range(n):
            word = queue.popleft()
            for i in range(len(word)):
                # for each i letter from the word, you will switch it for an ascii letter, that is,
                # ait, bit, cit, dit,...,hat, hbt, hct, ... hot
                for c in ascii_letters:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word not in words:
                        continue
                    if next_word == end:
                        return distance
                    # if the next_word is in the words set then append it to the queue and we start 
                    # from this next_word (dot)
                    if next_word in words:
                        print(next_word)
                        queue.append(next_word)
                        words.remove(next_word) # removing from the set is equivalent as marking the word visited
    return 0
 

def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = ladderLength(beginWord, endWord, wordList)
    print(res)

main()