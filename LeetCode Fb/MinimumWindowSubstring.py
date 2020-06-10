"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

f there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""

from collections import Counter

class Solution:
    def minWindow(self, s, substring):
        substringCounter, missing = Counter(substring), len(substring)
        internal_i = start = end = 0
        # 1 indicates that first letter will have index 1
        for index_char, char in enumerate(s, 1):
            # if the char is contained in the hash map (that's we use >0) then subtract 1 to missing
            missing -= substringCounter[char] > 0
            substringCounter[char] -= 1
            if not missing:
                # discard the previous window
                while substringCounter[s[internal_i]] < 0:
                    substringCounter[s[internal_i]] += 1
                    internal_i += 1
                # update the window with the new minimum window containing the chars
                if not end or index_char - internal_i <= end - start:
                    start, end = internal_i, index_char
                # reset missing to continue working in s
                substringCounter[s[internal_i]] += 1
                internal_i += 1
                missing += 1  # SPEEEEEEEED UP!
        return s[start: end]


def main():

    s = 'ADOBECODEBANC'
    t = 'ABC'
    solution = Solution()
    res = solution.minWindow(s,t)
    print(res)

main()