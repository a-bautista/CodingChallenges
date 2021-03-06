class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer because I want to find the middle letter
    # that will have at the left and right the same letters, so it is palindrome
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

def main():
    s = 'babad'
    solution = Solution()
    res = solution.longestPalindrome(s)
    print(res)

main()

'''
    Time complexity: O(N**2)
    Space complexity: O(1)
'''