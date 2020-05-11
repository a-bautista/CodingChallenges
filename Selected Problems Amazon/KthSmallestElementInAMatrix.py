"""
    O(k log k) time complexity.

    Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element
    in the matrix.

    We can start putting each element of the matrix in a heap and then we can traverse  the matrix and store the result
    and the coordinates of the matrix in i, j.
    Then we say that if i == 0 and j + 1< len(matrix) then get the next element in the matrix for the first row.
    if i+1 <len(matrix) then we again store the next element of the matrix for the second and third row.



"""

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1
        return result