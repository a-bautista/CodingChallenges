from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        dd = defaultdict(list)
        if not matrix:
            return result

        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        matrix_len = len(matrix)
        row_len =len(matrix[0])

        for i in range(0, matrix_len):
            for j in range(0, row_len):
                dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.

        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse() # reverse the order in the defaultdict
            result += dd[k] # rewrite the list
        return result

def main():

    matrix = [[2, 3, 5, 4],[7, 8, 1, 9],[1, 2, 4, 5]]
    solution = Solution()
    result = solution.findDiagonalOrder(matrix)
    print(result)


main()

"""
    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown 
    in the below image.
    
    [
        [2, 3, 5, 4],
        [7, 8, 1, 9],
        [1, 2, 4, 5]
    ]

"""