'''
    A simple implementation uses two iterations. In the first iteration, we add each
    element's value and its index to the table. Then, in the second iteration we check
    if each element's complement (target−nums[i]target - nums[i]target−nums[i])
    exists in the table.

    Beware that the complement must not be nums[i]nums[i]nums[i] itself!

    time complexity = O(n)
    space complexity = O(n)
'''

class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            if (nums[left]+nums[right]) == target:
                return [left, right]

            if nums[left]+nums[right] < target:
                left +=1
            if nums[left]+nums[right] > target:
                right -=1
        return [-1,-1]

        # d = {}
        # for i, n in enumerate(nums):
        #     # complement is how much is missing to achieve the target
        #     # if the complement is already in the dictionary, then we have found the two numbers
        #     # (x and complement that add up to the target).
        #     complement = target - n
        #     if complement in d:
        #         return [d[complement], i]
        #     else:
        #         d[n] = i
        #
        # # in case we didn't find the number
        # # we went through all the numbers and the dictionary contains all the elements
        # if len(d)==len(nums):
        #     return -1

def main():
    nums = [1,3,3,2,5]
    target = 5
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)

main()

'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''