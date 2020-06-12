"""
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
    Strings consists of lowercase English letters only and the length of both strings s and p will
    not be larger than 20,100.

    Input:
        s: "cbaebabacd" p: "abc"

    Output:
        [0, 6]

    Explanation:

        c b a e b a b a c d
        0 1 2 3 4 5 6 7 8 9

        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".

    Possible solution?

    Start iterating the array and verify if the i letter is contained in the p string.
    If the next i letter is contained in p then make sure that the next letter is again contained
    in the string.

"""

# class Solution:
#     def findAnagrams(self, s, p):
#         ns, np = len(s), len(p)
#         if ns < np:
#             return []
#
#         p_count, s_count = [0] * 26, [0] * 26
#         # build reference array using string p
#         for ch in p:
#             p_count[ord(ch) - ord('a')] += 1
#
#         output = []
#         # sliding window on the string s
#         for i in range(ns):
#             # add one more letter
#             # on the right side of the window
#             s_count[ord(s[i]) - ord('a')] += 1
#             # remove one letter
#             # from the left side of the window
#             if i >= np:
#                 s_count[ord(s[i - np]) - ord('a')] -= 1
#             # compare array in the sliding window
#             # with the reference array
#             if p_count == s_count:
#                 output.append(i - np + 1)
#
#         return output
#
#

from collections import Counter
class Solution:
    def findAnagrams(self, s, substring):

        ns, n_substring = len(s), len(substring)
        # constraint
        if ns < n_substring:
            return []

        # count the number of elements in the p string
        substring_count = Counter(substring)


        s_count = Counter()

        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter on the right side of the window
            s_count[s[i]] += 1
            # remove one letter from the left side of the window
            if i >= n_substring:

                if s_count[s[i - n_substring]] == 1:
                    # delete a letter from the left, so you can keep moving the window and you
                    # keep its size at len(substring) times
                    del s_count[s[i - n_substring]]
                else:
                    # subtract 1 value from the window
                    s_count[s[i - n_substring]] -= 1
            # compare array in the sliding window with the reference array
            # add the starting index
            if substring_count == s_count:
                output.append(i - n_substring + 1)

        return output

def main():
    solution = Solution()
    res = solution.findAnagrams('cbaebabacd', 'abc')
    print(res)

main()


"""
    Time complexity: O(len(s))
    Space complexity: O(k) where k is the size of the window
"""
