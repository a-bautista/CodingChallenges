'''
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order (ascending order).

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

[[0,0,0],[0,0,1],[0,1,1]]

[ 0 0 0
  0 0 1
  0 1 1 ]

Return 1 because in that column you will find the column with the value 1.

[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]

[
  0 0 0 0
  0 0 0 0
  0 0 0 1
  0 0 1 1
]

Return 2 because in that column you will find the column with the value 1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.


'''


#class BinaryMatrix(object):

#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) ->list []:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1


def main():
    # binaryMatrix = BinaryMatrix()
    # binaryMatrix.

    l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
    solution = Solution()
    res = solution.leftMostColumnWithOne(l)
    print(res)


main()

# Time complexity: O(M+N), M is number of rows and N is number of columns.
# Therefore, we'll stay in the grid for at most N+M steps, and therefore get a time complexity of O(N + M)
# Space complexity: O(1)