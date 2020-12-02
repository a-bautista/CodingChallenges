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


    # def solve(nums, target):
    #     seen = set()
    #     output = set()
    #
    #     for i in range(len(nums)):
    #         num1 = target - nums[i]
    #
    #         if num1 not in seen:
    #             seen.add(nums[i])
    #         else:
    #             output.add((min(nums[i], num1), max(nums[i], num1)))
    #
    #     if len(output) == 0:
    #         return -1
    #
    #     return output

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