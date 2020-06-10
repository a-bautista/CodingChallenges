"""
    Given a string, find the length of the longest substring T that contains at most k distinct characters.

    Example 1:

    Input: s = "eceba", k = 2
    Output: 3
        Explanation: T is "ece" which its length is 3.

    Example 2:

    Input: s = "aa", k = 1
    Output: 2
        Explanation: T is "aa" which its length is 2.

"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str', k: int) -> int:
        n = len(s)

        # edge case
        if n == 0 or k == 0:
            return 0

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1

        while right < n:
            # add new characters and move right pointer
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains k + 1 characters, delete the character with the lowest value
            if len(hashmap) > k :
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len


def main():
    s = 'cceebazy'
    k = 3
    solution = Solution()
    res = solution.lengthOfLongestSubstringTwoDistinct(s, k)
    print(res)

main()

"""
    For the best case when input string contains not more than k distinct characters the answer is yes. 
    It's the only one pass along the string with N characters and the time complexity is O(N)\mathcal{O}(N)O(N).

For the worst case when the input string contains n distinct characters, the answer is no. In that case at each step one uses O(k)\mathcal{O}(k)O(k) time to find a minimum value in the hashmap with k elements and so the overall time complexity is O(Nk)\mathcal{O}(N k)O(Nk).

    Time complexity : O(N)\mathcal{O}(N)O(N) in the best case of k distinct characters in the string and 
    O(Nk)\mathcal{O}(N k)O(Nk) in the worst case of N distinct characters in the string.

    Space complexity : O(k)\mathcal{O}(k)O(k) since additional space is used only for a hashmap with 
    at most k + 1 elements. 

"""