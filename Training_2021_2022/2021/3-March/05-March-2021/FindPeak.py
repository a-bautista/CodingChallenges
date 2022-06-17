'''
    A peak element is an element that is greater than its neighbors.

    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
'''

def solve(nums):
    left =0
    right= len(nums)-1

    while left<=right:
        mid = left + (right - left) //2
        if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
            return mid
        elif nums[mid+1]>nums[mid]:
            left =mid +1
        else:
            right=mid - 1
    # [1,2,3,4,1] so let's say nums[left] is 4 and nums[right] is 1, then return nums[left] because nums[left] is greater 
    # than nums[right]
    return left if nums[left]>=nums[right] else right

def main():
    nums = [1,2,3,4,1]
    res = solve(nums)
    print(res)

main()