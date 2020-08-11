'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.


'''
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # get the first elements of each sorted array
        # we will have value, row and column
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        res = 0
        # convert the list to a heap
        heapq.heapify(heap)
        # stop when _ is equal to k
        for _ in range(k):
            ret, row, col = heapq.heappop(heap)
            # verify if it is possible to keep moving to the right
            if (col + 1) < len(matrix[0]):
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
        return res



'''
    The idea behind this is that you need to always keep the smallest element
    in the heap and you will pop it at k times, so that will give the smallest
    element in the matrix.
     O(k * log n), so the worst-case and average-case time complexity is 
     O(n^2 * log n). 
     Space complexity is O(n).
'''


# def kthSmallest(self, matrix, k: int) -> int:
#     lo, hi = matrix[0][0], matrix[-1][-1]
#     while lo < hi:
#         # Calculating mid element of sorted array
#         mid = (lo + hi) // 2
#         # bisect.bisect_right(iterable, element) gives index of first element that is greater than the targeted value.
#         # Similarly bisect.bisect_left(iterable, element) gives index of first element that is greater than or equal to the targeted value.
#         # In the context, bisect.bisect_right(row, mid) gives the index where first element that would be greater than mid.
#         # This bisect.bisect_right(row, mid) is calculated for all the rows of the matrix to get indices of first element in each row which is greater than mid.
#         # Summing up these indices would give us the total number of elements that are less than or equal to mid.
#         # If number of such elements less than calculated mid is <k then we reduce the search space by increasing low=mid+1 (because for mid we've seen that number of elements <= mid are <k)
#         # If number of elements less than calculated mid is >=k then we reduce the search space by bringing down high=mid
#         if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
#             lo = mid + 1
#         else:
#             hi = mid
#     return lo
# Time complexity: O(n * log(n))
# Space complexity: Constant O(1)