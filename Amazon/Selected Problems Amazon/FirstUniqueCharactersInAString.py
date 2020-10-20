
"""
    The idea is to go through the string and save in a hash map the number of times each character appears in the string.
    That would take O(N) time, where N is a number of characters in the string.

    And then we go through the the hash map and start checking if the index is 1 to check if that's the unique character.

    Time complexity: O(N) since we go to the length of N
    Space complexity: O(N)

"""


import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1