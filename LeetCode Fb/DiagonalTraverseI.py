"""
    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown
    in the below image.

    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]

    [1,2,4,7,5,3,6,8,9]

"""

from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # test case
        if not matrix:
            return []

        matrix_len = len(matrix)
        col_len    = len(matrix[0])

        res = []
        lines = defaultdict(list)

        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        # this is the data structure that I want to achieve for [[2, 3, 5, 4],[7, 8, 1, 9],[1, 2, 4, 5]]
        # 0:[2], 1:[3,7], 2:[5,8,1], 3:[4,1,2], 4:[9,4], 5:[5]

        for row in range(matrix_len):
            for col in range(col_len):
                lines[row+col].append(matrix[row][col])

        # Step 2: We need to reverse the rows that are even
        # 0:[2], 1:[3,7], 2:[5,8,1], 3:[4,1,2], 4:[9,4], 5:[5], so rows 0,2,4
        for k in range(matrix_len + col_len - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res

def main():

    matrix1 = [[2, 3, 5, 4],[7, 8, 1, 9],[1, 2, 4, 5]]
    matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
    # result of matrix1
    # [2, 3, 7, 1, 8, 5, 4, 1, 2, 4, 9, 5]
    # result of matrix2
    # [1, 2, 4, 7, 5, 3, 6, 8, 9]

    solution = Solution()
    result = solution.findDiagonalOrder(matrix1)
    print(result)


main()

'''
    Time complexity: 
    O(m*n)
    Space complexity:
    O(m*n)
'''