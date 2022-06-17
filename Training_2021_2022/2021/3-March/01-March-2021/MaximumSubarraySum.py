'''
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum
    and return its sum.

    Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Intro to DP?
'''

def solve(nums):

    n = len(nums)
    current_sum = max_sum = nums[0]

    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = solve(nums)
    print(res)

main()