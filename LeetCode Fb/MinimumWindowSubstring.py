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

# class Solution:
#     def minWindow(self, s, substring):
#         substringCounter, missing = Counter(substring), len(substring)
#         internal_i = start = end = 0
#         # 1 indicates that first letter will have index 1
#         for index_char, char in enumerate(s, 1):
#             # if the char is contained in the hash map (that's we use >0) then subtract 1 to missing
#             missing -= substringCounter[char] > 0
#             substringCounter[char] -= 1
#             if not missing:
#                 # discard the previous window
#                 while substringCounter[s[internal_i]] < 0:
#                     substringCounter[s[internal_i]] += 1
#                     internal_i += 1
#                 # update the window with the new minimum window containing the chars
#                 if not end or index_char - internal_i <= end - start:
#                     start, end = internal_i, index_char
#                 # reset missing to continue working in s
#                 substringCounter[s[internal_i]] += 1
#                 internal_i += 1
#                 missing += 1  # SPEEEEEEEED UP!
#         return s[start: end]


def find_substring(str1, pattern):
  window_start, matched, substr_start = 0, 0, 0
  min_length = len(str1) + 1
  char_frequency = {}

  # count the frequency of each char in the pattern to find
  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # try to extend the range [window_start, window_end] from the string
  # Just make the window bigger to contain all the chars from the pattern
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] >= 0:  # Count every matching of a character
        matched += 1

    # Shrink the window if we can to match the pattern in the string. Min lenght captures the index of the ending
    # pattern of the string whereas window_start captures the index where the pattern begins. Once the pattern
    # has been captured, remove a matched character to continue moving into the rest of characters of the string.
    while matched == len(pattern):
      if min_length > window_end - window_start + 1:
        min_length = window_end - window_start + 1
        substr_start = window_start

      left_char = str1[window_start]
      # move onto the next char from the string, and in case we have redundant chars then delete them, so we can
      # get out of the loop
      window_start += 1
      if left_char in char_frequency:
        # Note that we could have redundant matching characters, therefore we'll decrement the
        # matched count only when a useful occurrence of a matched character is going out of the window,
        # matched-=1 is there to stop coutning the match
        if char_frequency[left_char] == 0:
          # decrease the matched to go out from the loop
          matched -= 1
        # Indicate in which letter from the pattern you stopped when you found it in the string,
        # so next time you find this letter then you know you have found the pattern again
        char_frequency[left_char] += 1

  if min_length > len(str1):
    return ""
  return str1[substr_start:substr_start + min_length]


def main():
  # print(find_substring("aabdec", "abc"))
  # print(find_substring("abdabca", "abc"))
  # print(find_substring("adcad", "abc"))
  # print(find_substring("ADOBECODEBANC", "ABC"))
  print(find_substring("ADOBEDCBANC", "ABC"))

main()


# def main():
#
#     s = 'ADOBECODEBANC'
#     t = 'ABC'
#     solution = Solution()
#     res = solution.minWindow(s,t)
#     print(res)
#
# main()

"""
    Time complexity: O(N+M)
    Space complexity: O(M) because in the worst case, the whole pattern can 
    have distinct characters which will go in the hashmap.
"""