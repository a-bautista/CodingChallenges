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

def productExceptSelf(nums):
    ans = [1 for _ in nums]
    left = 1
    right = 1

    for i in range(len(nums)):
        ans[i] *= left
        ans[-1 - i] *= right
        left *= nums[i]
        right *= nums[-1 - i]

    return ans

def main():
    nums = [2,3,4,5]
    #solution = Solution()
    res = productExceptSelf(nums)
    print(res)

main()

"""
    Python solution (Accepted), O(N) time, O(1) space
"""