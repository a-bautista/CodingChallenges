'''
    Given an array of integers, return indices of the two numbers such that they add up to a
    specific target.

    You may assume that each input would have exactly one solution, and you may not use the
    same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''
class Solution:
    def solve(self, nums, target):
        nums.sort()

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

def main():
    nums = [4,7,8,53,56]
    target = 15
    solution = Solution()
    res = solution.solve(nums, target)
    print(res)

main()