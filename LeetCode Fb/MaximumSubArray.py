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

