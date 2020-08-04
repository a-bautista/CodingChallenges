'''
    S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

    S was sorted in some custom order previously. We want to permute the characters of T so that they match
    the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the
    returned string.

    Return any permutation of T (as a string) that satisfies this property.

    Example :
    Input:
    S = "cba"
    T = "abcd"
    Output: "cbad"
    Explanation:
    "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
    Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

'''

from collections import Counter

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)

'''
    Time complexity: O(S.length+T.length)
    Space complexity: O(T.length)
'''