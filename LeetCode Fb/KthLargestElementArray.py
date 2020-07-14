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
        
class Solution:
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        new_k = len(nums) + 1 - k
        return self.findKthSmallest(nums, new_k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            # go to the right side
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            # go to the left side
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            # we found the pivot
            else:
                return nums[pos]

    # choose the right-most element as pivot
    # l should be the value with kth largest element 
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


def main():
    nums = [3,9,3,1,2,4,8,5,6]
    k = 3
    solution = Solution()
    res = solution.findKthLargest(nums, k)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
    
    Quick select algorithm:
        You need to provide a pivot, so we generate a partitioned list where every element in the left side is less than
        the pivot and every element in the right side is greater than the pivot. 
        
        If index of partitioned element (pivot) is more than k, then we recur for left part. If index (pivot) is same 
        as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for right part. 
'''

