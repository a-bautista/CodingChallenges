from collections import Counter, deque
from heapq import *

def solve(words, k):
    counter = Counter(words)
    res = []
    freqWords = []
    for word, count in counter.items():
        heappush(res, (-count, word))
        # if len(res)>k:
        #      freqWords.append(heappop(res)[1])
    # for _ in range(k):
    #     freqWords.append(res[1])
    # return freqWords
    return [heappop(res)[1] for _ in range(k)]



def main():
    words = ["a","a","a", 
             "b","b","b",
             "love", "love","love", 
             "you"]
    k = 2
    res = solve(words, k)
    print(res)

main()