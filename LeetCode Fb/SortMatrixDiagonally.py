'''
    Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right
    then return the sorted array.

    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

    Constraints:

        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        1 <= mat[i][j] <= 100
'''
from collections import defaultdict
def diagonalSort(matrix):

    diags = defaultdict(list)

    # get all the diagonals
    for i, row in enumerate(matrix):
        for j, a in enumerate(row):
            diags[i-j].append(a)

    # reverse each diagonal
    for diag in diags.values():
        diag.sort(reverse=True)

    # replace each reversed diagonal in the matrix
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            matrix[i][j] = diags[i-j].pop()
    return matrix

def main():
    matrix = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    res = diagonalSort(matrix)
    print(res)

main()


'''
    Time complexity: O(mn log(min(m,n))
    Space complexity: O(Mn)
'''