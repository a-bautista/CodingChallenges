"""
    Given two arrays, write a function to compute their intersection.

    Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

"""
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # keep the heap of size k and store elements from largest to smallest
        # bring me the last element which is the kth element
        return heapq.nlargest(k, nums)[-1]

def main():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solution = Solution()
    res = solution.findKthLargest(nums, k)
    print(res)

main()

"""
    Time complexity : O(N *log (k)).
    Space complexity : O(k) to store the heap elements. 
"""