"""
    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
    of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]

    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
    (including the whole array) fits in a 32 bit integer.

    Note: Please solve it without division and in O(n).

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        # start in n-1, stop at -1 and reduce by -1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


def main():
    nums = [2,3,4,5]
    solution = Solution()
    res = solution.productExceptSelf(nums)
    print(res)

main()

"""
    Python solution (Accepted), O(n) time, O(1) space
"""