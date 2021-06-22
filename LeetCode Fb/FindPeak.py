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

class Solution:
    def findPeak(self, nums):
        # declare the pointers
        left = 0
        right = len(nums)-1

        # do the binary search because it is sorted
        while left < right:
            mid = left + (right -left)//2
            # if the middle number is greater than the next element and the middle number is also greater than the
            # previous element then we found the peak element
            if nums[mid] > nums[mid+1] and nums[mid]> nums[mid-1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                left = mid +1
            else:
                right = mid-1
        # if the array length contains 2 elements and the left element is greater
        # than the right one then return the left else return the right
        # which means only 1 element is in the array.

        return left if nums[left] >= nums[right] else right

def main():

    nums = [1,2,3,1]
    solution = Solution()
    res = solution.findPeak(nums)
    print(res)

main()

'''
    Time complexity: O(Log(N)) because it is binary search
    Space complexity: O(1)
    
    Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half

Run time: O(logn)
Memory: constant
Test cases: 
     [1]
     [1,2]
     [2,1]
     [1,2,3]
     [3,2,1]
     [2,1,3]
'''