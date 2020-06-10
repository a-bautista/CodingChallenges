"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000


Time/Space: log(b)

"""


class Solution(object):
    def pow(self, a, b):
        if b < 0:
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)

    def helper(self, a, b):
        if b == 0:
            return 1
        half = self.helper(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

def main():
    solution = Solution()
    res = solution.pow(2,10)
    print(res)


main()