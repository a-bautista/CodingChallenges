"""
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

    Example 2:

    Input: "race a car"
    Output: false

    Two pointers approach:

        If you compare each letter of the string starting from 0 and from the end and each letter is the same,
        then the string is a palindrome.
"""

class Solution:
    def valid(self, s):
        start, end = 0, len(s)-1
        while (start < end):
            # if you find a comma or space, then increase start by 1
            # until you find a letter, then exit the loop
            while start < end and not s[start].isalnum():
                start += 1
            # if you find a comma or space, then increase start by 1
            # until you find a letter, then exit the loop
            while start < end and not s[end].isalnum():
                end -= 1
            # if a letter is distinct from the start and end, then the word is not a palindrome
            if start < end and s[start].lower() != s[end].lower():
                return False

            start += 1
            end   += 1

        return True

def main():
    s = ['A man, a plan, a canal: Panama']
    solution = Solution()
    res = solution.valid(s)
    print(res)

main()


"""
    Time complexity: O(N)
    Space complexity: O(1)
"""