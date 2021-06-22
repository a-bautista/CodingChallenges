'''
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

'''
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, lookLeftIndex):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (lookLeftIndex and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        return lo


    def searchRange(self, nums, target):
        # first look for the left index
        left_idx = self.extreme_insertion_index(nums, target, True)

        # If the left index didn't find the target value then just return -1
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        # look for the right index and when found, don't forget to subtract -1 to stay
        # in the bounds of the array
        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

# class Solution:
#     # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
#     # array `nums` via binary search.
#     def extreme_insertion_index(self, nums, target):
#         lo = 0
#         hi = len(nums)
#
#         while lo < hi:
#             mid = lo + (hi - lo) // 2
#             if nums[mid] >= target:
#                 hi = mid
#             else:
#                 lo = mid+1
#         return lo
#
#
#     def searchRange(self, nums, target):
#         # first look for the left index
#         left_idx = self.extreme_insertion_index(nums, target)
#
#         if left_idx in nums:
#             return [left_idx, self.extreme_insertion_index(nums, target) - 1]
#         else:
#             # If the left index didn't find the target value then just return -1
#             #if left_idx == len(nums) or nums[left_idx] != target:
#             return [-1, -1]
#
#         # look for the right index and when found, don't forget to subtract -1 to stay
#         # in the bounds of the array
#         #return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

def main():
    nums = [2,2]
    target = 3
    nums2 = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    target2 = 2
    solution = Solution()
    res = solution.searchRange(nums2, target2)
    print(res)

main()

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''