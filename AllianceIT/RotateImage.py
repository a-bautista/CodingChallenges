'''

    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:

        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.

    Given input matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

        rotate the input matrix in-place such that it becomes:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]

'''


class Solution:
    def rotate(self, matrix):
        """
            Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        externalLoop = (n // 2 + n % 2)
        internalLoop = (n // 2)
        for i in range(externalLoop):
            for j in range(internalLoop):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements clockwise
                for k in range(4):
                    matrix[row][col] = tmp[(k-1) % 4]
                    row, col = col, n - 1 - row

                # rotate 4 elements counter -clockwise
                # for k in range(4):
                #     matrix[row][col] = tmp[(k + 1) % 4]
                #     row, col = col, n - 1 - row

        print(matrix)

    def simpleSol(self, matrix):
        # reverse the matrix
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                # do a swap of elements by symmetry
                # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                # [[7, 8, 9] then 8 and 4 are changed,2 and 6 are changed and 9 and 1
                #  [4, 5, 6]
                #  [1, 2, 3]
                # ]
                #
                #
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]

        print(matrix)



def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]]
    #matrix = [[1, 2], [3, 4]]
    solution = Solution()
    #solution.rotate(matrix2)
    solution.simpleSol(matrix)


main()

'''
    Time complexity: O(N**2)
    Space complexity: O(1) because we do the rotation in place and allocate only the list of 4 elements
    as temporary helper
'''