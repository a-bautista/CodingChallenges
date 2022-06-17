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
    The solution from below works for m*m matrices, not for m*n because of the transpose.
'''
class Solution:
    def rotate(self, matrix):
        self.transpose(matrix)
        self.reverse(matrix)
    
    
    def transpose(self, matrix):
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        
    def reverse(self, matrix):
        for row in range(len(matrix)):
            # len(matrix)//2 will provide a value of 1 
            for col in range(len(matrix)//2):
                # 
                matrix[row][col], matrix[row][-col-1] = matrix[row][-col-1], matrix[row][col]

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    solution.rotate(matrix)
    print(matrix)

main()


'''
    Time complexity: O(M) because we are moving the cell at least once and then we reverse which has a cost
    of O(M) because we are moving the value of each cell once.
    Space complexity: O(1)
'''