'''
<<<<<<< HEAD:LeetCode Fb/SearchRotatedArrayII.py

=======
>>>>>>> 16c42ef55622b5f383005ce9b09fd589a55fa8f6:LeetCode Fb/SearchRotatedArrayII.py
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

'''

class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            ##### double binary search because the array has been rotated ######
            # target is in the second half
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # target is in the first half
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target
        
def main():

    nums = [2,5,6,0,0,1,2]
    solution = Solution()
    res = solution.search(nums, 6)
    print(res)

main()

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''
