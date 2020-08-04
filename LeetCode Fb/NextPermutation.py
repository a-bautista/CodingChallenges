# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         # find longest non-increasing suffix
#         right = len(nums) - 1
#         while nums[right] <= nums[right - 1] and right - 1 >= 0:
#             right -= 1
#         if right == 0:
#             return self.reverse(nums, 0, len(nums) - 1)
#         # find pivot
#         pivot = right - 1
#         successor = 0
#         # find rightmost succesor
#         for i in range(len(nums) - 1, pivot, -1):
#             if nums[i] > nums[pivot]:
#                 successor = i
#                 break
#         # swap pivot and successor
#         nums[pivot], nums[successor] = nums[successor], nums[pivot]
#         # reverse suffix
#         self.reverse(nums, pivot + 1, len(nums) - 1)
#         return nums
#
#     def reverse(self, nums, l, r):
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        left = len(nums) - 2

        # use this cycle to find the largest number in the array from left to right
        while (left >= 0) and nums[left] >= nums[left + 1]:
            left -= 1

        # reverse the list
        self.reverse(nums, left+1, len(nums)-1)

        # this means that I went through the entire array and all elements were from the
        # highest to the lowest number, thus return the reversed list
        if left == -1:
            return nums

        # locate the index of numbers for doing the swap
        right = left + 1
        while right < len(nums) and nums[left] >= nums[right]:
            right += 1

        # swap the elements
        nums[left], nums[right] = nums[right], nums[left]
        return nums

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

def main():
    solution = Solution()
    res = solution.nextPermutation([5,4,3,2,1])
    #res = solution.nextPermutation([1,7,9,9,8,3])
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''