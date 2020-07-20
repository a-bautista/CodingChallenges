'''

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone
decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

'''

def solve(nums):
    increasing = decreasing = True
    for i in range(len(nums) - 1):
        if nums[i]> nums[i+1]:
            decreasing = False
        if nums[i]<nums[i+1]:
            increasing = False
    return increasing or decreasing

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''