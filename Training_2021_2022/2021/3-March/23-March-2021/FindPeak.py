'''
    A peak element is an element that is greater than its neighbors.

    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

    I get the middle number and I compare with left and right. If the middle number is greater
    than nums[middle+1] and it is less than nums[middle-1] then I found my element.

    elif middle > nums[left] then I move my left pointer to middle because
    I didn't find any peak element.
    left = middle + 1
    
    else move my right pointer to mid because I didn't find my number on the right side
    right = middle -1
    to the 
'''

def solve(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid]>nums[mid+1] and nums[mid-1]<nums[mid]:
            return nums[mid]
        elif nums[mid]>nums[left]:
            left = mid + 1
        else:
            right = mid -1
    return left if nums[left]>=nums[right] else right
    

def main():
    #nums = [1,2,3,1,2]
    nums2 = [0, 10, 0]
    res = solve(nums2)
    print(res)

main()


