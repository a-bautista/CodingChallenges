'''
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.

    Example 1:

    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
    Example 2:

    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        cnt_palindrome = 0
        
        for i in reversed(range(len(s))):
            for dist in range(len(s)):
                if i + dist < len(s):
                    j = i + dist
                    if i == j:
                        dp[i][j] = True
                    elif i + 1 == j:
                        dp[i][j] = s[i] == s[j]
                    else:
                        dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                    if dp[i][j]:
                        cnt_palindrome += 1
        return cnt_palindrome


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        table = [[False for x in range(n)] for y in range(n)]
        count = 0

        # Every isolated char is a palindrome
        for i in range(n):
            table[i][i] = True
            count += 1

        # Check for a window of size 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        # Check windows of size 3 and more
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1

        return count