'''
    Constraints:
    0. I want to get the index of numbers. Solved
    1. Unique pair or multiple pairs? Let it be unique because we are following a binary search approach. Solved.
    2. If a number is not found then return -1. solved
    3. Complexity O(N) in time. Solved
    4. Check for errors

    time complexity = O(n)
    space complexity = O(n)
'''


def twoSum(nums, target):
    if len(nums)>0:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] == target:
                return [left, right]

            if nums[left] + nums[right] < target:
                left += 1

            if nums[left] + nums[right] > target:
                right -= 1
        return [-1, -1]
    else:
        raise ValueError('No numbers were given')
        exit(-1)

def main():
    nums = []
    target = 3
    solution = twoSum(nums, target)
    print(solution)

main()