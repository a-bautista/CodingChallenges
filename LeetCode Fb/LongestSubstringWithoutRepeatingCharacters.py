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
#    def lengthOfLongestSubstring(self, s: str) -> int:
#         used = {}
#         max_length = start = 0
#         for i, c in enumerate(s):
#             if c in used and start <= used[c]:
#                 # indicate where was the last poisition of the index
#                 start = used[c] + 1
#             else:
#                 # add the length of the current index (total) - the last index that you had (existing content) + 1 (new val)
#                 max_length = max(max_length, i - start + 1)
#             # check where was the last index
#             used[c] = i
#         return max_length



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        sub = ''
        
        for char in s:
            # start adding each different char to the window
            if char not in sub:
                sub += char
                # calculate the length of the window and determine if the window is greater than ans
                ans = max(ans, len(sub))
            # if the char already exists in the window
            else:
                # determine where is located this char in the window
                cut = sub.index(char)
                # cut the window from that char that you found and start a new window with this new chart
                sub = sub[cut + 1:] + char
        return ans
        
'''
    Time complexity: O(N)
    Space complexity: O(k)
'''