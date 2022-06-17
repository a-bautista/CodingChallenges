'''
    Given a string paragraph and a string array of the banned words banned, return the most frequent word 
    that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

    The words in paragraph are case-insensitive and the answer should be returned in lowercase.
    Example 1:

    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"
    Explanation: 
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"), 
    and that "hit" isn't the answer even though it occurs more because it is banned.

'''

from heapq import *
from collections import Counter
def solve(str1, banned):
    #1) lower case 
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in str1])
    
    #2). split the string into words
    words = normalized_str.split()

    counter = Counter(words)
    #print((counter))

    res = []
    count = {}

    #print(counter)
    for word, freq in counter.items():
        if word not in banned:
            heappush(res, (-freq, word))

    return res[0][1]

    # return res[0][1]
    # #print(counter)
    # #print(words)
    # lowStr1 = str1.lower().split(" ")
    
    # #print(lowStr1.split())
    # count = {}
    # count2 = Counter(lowStr1).most_common
    # #print(count2)
    # res = []
    # # invalid chars that can be added to the string
    # setOfInvalidChars = set(chr(x) for x in range(33, 64))
    
    # for word in lowStr1:
    #     if word in setOfInvalidChars:
    #         print(word.split(","))


    #     if word[-1] in setOfInvalidChars or word[0] in setOfInvalidChars:
    #     #if word.endswith(".") or word.endswith(",") or word.endswith(";") or word.startswith(","):
    #         word = word[:len(word)-1]
    #     if word not in banned:
    #         if word not in count:
    #             count[word]=1
    #         else:
    #             count[word]+=1
        
    # for word, freq in count.items():
    #     heappush(res, (-freq, word))

    # return res[0][1]

def main():
    s = "Bob hit a ball, the hit BALL flew far after it was hit."
    s2 = "a, a, a, a, b,b,b,c, c"
    banned = ["hit"]
    res = solve(s, banned)
    print(res)

main()