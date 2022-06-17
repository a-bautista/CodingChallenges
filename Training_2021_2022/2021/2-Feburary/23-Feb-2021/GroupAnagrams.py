'''
    Given an array of strings, group anagrams together.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

    Note:
        All inputs will be in lowercase.
        The order of your output does not matter.
                                key              values
    ["ate","eat","tea"] = (1,0,0,0,1,...):["ate", "eat", "tea"]

'''
from collections import defaultdict
def solve(words):
    d = defaultdict(list)
    for word in words:
        key = [0] * 26
        for s in word:
            key[ord(s) - ord('a')] += 1
        d[tuple(key)].append(word)
    return d.values()

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = solve(words)
    print(sol)

main()

