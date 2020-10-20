"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]
"""

from collections import defaultdict
def solve(strs):
    d = defaultdict(list)

    for word in strs:
        counter = [0]*26

        for l in word:
            counter[ord(l)-ord('a')]+=1
        d[tuple(counter)].append(word)
    return d.values()


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solve(strs))

main()



'''
    Time complexity: O(N*k)
    Space complexity: O(N*k)
'''
