'''Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5


[6, 5, 4, 3, 2, 1] k=2
 1  2  3  4  5  6
Output = 5


Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4


'''

import heapq


def main():
    l  = [3,2,1,5,6,4]
    l2 = [3,2,3,1,2,4,5,5,6]
    solution = Solution.findKthLargest(Solution,l,2)
    solution2 = Solution.findKthLargest(Solution, l2, 4)
    print(solution)
    print(solution2)



class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1] # bring the last element

if __name__ == '__main__':
    main()