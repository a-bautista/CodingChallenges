'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



'''

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         ans = 0
#         sub = ''
#         for char in s:
#             if char not in sub:
#                 sub += char
#                 ans = max(ans, len(sub))
#             else:
#                 cut = sub.index(char)
#                 sub = sub[cut + 1:] + char
#         return ans

class Solution:
    def lengthOfLongestSubstring(self, string):
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest