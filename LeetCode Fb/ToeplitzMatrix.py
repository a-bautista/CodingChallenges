# def isToeplitzMatrix(m):
#     for i in range(len(m) - 1):
#         for j in range(len(m[0]) - 1):
#             if m[i][j] != m[i + 1][j + 1]:
#                 return False
#     return True

'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.



'''

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for index_row, row in enumerate(matrix):

            for index_col, val in enumerate(row):

                if index_row-index_col not in groups:
                    groups[index_row-index_col] = val

                elif groups[index_row-index_col] != val:
                    return False
        return True


def main():
    matrix = [[1, 2, 3, 4],[5, 1, 2, 3],[9, 5, 1, 2]]
    solution = Solution()
    res = solution.isToeplitzMatrix(matrix)
    print(res)

main()

'''
    Time complexity: O(M*N) because M and N are the number of rows and columns.
    Space complexity: O(M+N)
'''