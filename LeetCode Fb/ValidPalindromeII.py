"""
    Given a non-empty string s, you may delete at most one character.
    Judge whether you can make it a palindrome.

    Example 1:

    Input: "aba"
    Output: True

    Example 2:

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

"""

class Solution:
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     # Time: O(n)
    #     # Space: O(n)
    #     left, right = 0, len(s) - 1
    #     while left < right:
    #         if s[left] != s[right]:
    #             one, two = s[left:right], s[left + 1:right + 1]
    #             # [::-1] indicates to invert string
    #             # second last letter, i.e., [bi] -> [ib]
    #             print(one)
    #             #print(one == one[::-1])
    #             print(two)
    #             print(two[::-1])
    #             return one == one[::-1] or two == two[::-1]
    #         left, right = left + 1, right - 1
    #     return True

    def validPalindrome(self, s):
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) \
                       or self.validPalindromeUtil(s, i, j - 1)
        return True

    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


def main():
    s = 'abbia'
    solution = Solution()
    res = solution.validPalindrome(s)
    print(res)

main()

'''
    abbia
    a = a
    b != i so one = 'bb' and two = 'bi' 
    one[::-1] = 'bb'
    two[::-1] = 'ib'
    
    final result is abiba which is palindrome 
    
    Time complexity: O(N)
    Space complexity: O(N)
    

'''