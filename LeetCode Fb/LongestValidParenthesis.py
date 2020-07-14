'''
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
    parentheses substring.

    Example 1:

    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"

    Example 2:

    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"


'''
#
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_len, R = 0, range(len(s))
#         for d, iterator in enumerate((R, reversed(R))):
#             l, r = 0, 0
#             for i in iterator:
#                 l += s[i] == '('
#                 r += s[i] == ')'
#                 if l == r:
#                     max_len = max(max_len, l)
#                 elif d ^ (l < r):
#                     l, r = 0, 0
#         return 2 * max_len


def longestValidParentheses(s):
    # we use len(s) + 1 to indicate that in the last position we
    # will insert the result of the longest valid substring parenthesis

    dp, stack = [0]*(len(s) + 1), []


    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                # p will contain the index where you encountered a ')'
                p = stack.pop()
                # dp[i + 1] is used to store the longest valid parenthesis substring count
                # d[p] contains the count of what you currently had when you found an ()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)


def main():
    res = longestValidParentheses("(()()")
    print(res)

main()
'''
    Time complexity: O(N)
    Space complexity: O(N)
'''