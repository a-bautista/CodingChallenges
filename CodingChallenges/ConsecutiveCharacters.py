'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains
only one unique character.

Return the power of the string.

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Input: s = "triplepillooooow"
Output: 5

'''

# leetcode Solution
class Solution2:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                # if same as previous one, increase the count
                count += 1
            else:
                # else, reset the count
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count

# my solution
class Solution:
    def maxPower(self, s: str) -> int:

        # edge case when there's not any letter
        if not len(s):
            return -1

        # edge case when there's only 1 letter
        if len(s) == 1:
            return 1

        max_count = 1
        start = 0
        previous = end = 1

        while end <= len(s):
            if s[start] == s[previous]:
                # remember that the end is not inclusive
                max_count = max(max_count, len(s[start:end]))
            else:
                start = previous
            previous = end
            end += 1
        return max_count


def main():
    solution = Solution()
    res = solution.maxPower('leeetcode')
    print(res)


main()