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

'''

from collections import defaultdict
class Solution:
    def solve(self,strs):
        # create the defaultdict that will store the numeric positions in a tuple
        # and the string values assigned to it
        d = defaultdict(list)

        for s in strs:
            # create the counter that holds each position of each string s
            counter = [0]*26
            for char in s:
                # assign a 1 to the position of each letter
                counter[ord(char)-ord('a')] +=1
            # assign the counter to the dict with the corresponding string s
            # use a tuple to avoid the unhashable type error
            d[tuple(counter)].append(s)
        return d.values()

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.solve(strs)
    print(res)

main()

'''
    Time complexity: O(N*k)
    Space complexity: O(N*k)
'''