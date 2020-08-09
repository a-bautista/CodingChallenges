'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


'''

def solve(nums):
    n = len(nums)
    max_sum = curr_sum = nums[0]

    for i in range(n):
        curr_sum = max(curr_sum, curr_sum+ nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''

