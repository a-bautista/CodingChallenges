"""
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
    the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""

class Solution:
    def moveZeroes(self, nums):

        # edge case: verify if all elements are zero
        if len(set(nums)) < 1:
            return nums

        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums


def main():
    #nums = [0,0,0,0,1]
    nums2 = [2,1,7,3,0,1]
    nums = [0,1,1,0,1]
    solution = Solution()
    res = solution.moveZeroes(nums)
    print(res)

main()


"""
    Time complexity: O(n)
    Space complexity: O(n)
"""