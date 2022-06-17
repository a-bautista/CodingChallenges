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
# def lengthOfLongestSubstring(s):
#     used = {}
#     max_length = start = 0
#     for i, c in enumerate(s):
#         if c in used and start <= used[c]:
#             # indicate where was the last poisition of the index
#             start = used[c] + 1
#         else:
#             # add the length of the current index (total) - the last index that you had (existing content) + 1 (new val)
#             max_length = max(max_length, i - start + 1)
#         # check where was the last index
#         used[c] = i
#     return max_length

def lengthOfLongestSubstring(str1):
    pattern  = ''
    windowStart, maxLength = 0,0
    for windowEnd in range(len(str1)):
        if str1[windowEnd] not in pattern:
            pattern += str1[windowEnd]
            maxLength = max(maxLength, len(pattern))
        else:
            # in case there's a letter in our pattern
            # get the index where that letter is located in our pattern
            windowStart = pattern.index(str1[windowEnd])
            # sub[windowStart+1:] removes the current letters of sub and add the new letter in our pattern
            pattern = pattern[windowStart+1:]+str1[windowEnd]
    return maxLength


def main():
    s = 'abcabcbb'
    s1 = 'araaci' # aci

    res = lengthOfLongestSubstring(s1)
    print(res)


main()

'''
    Time complexity: O(N)
    Space complexity: O(k)
'''