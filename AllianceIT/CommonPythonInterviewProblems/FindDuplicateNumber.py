'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least
one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

'''

class Solution(object):
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while high - low > 1:
            count = 0
            # count if duplicates are located in the window
            # mid and high
            for k in nums:
                if mid < k <= high:
                    count += 1
            # move the low pointer
            if count > high - mid:
                low = mid
            # move the right pointer
            else:
                high = mid
            mid = (high + low) // 2
        return high


'''
    Time complexity: O(n*log(n))
    Space: O(1)
'''