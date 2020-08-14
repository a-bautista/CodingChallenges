'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]


'''

class Solution(object):
    def spiralOrder(self, matrix):
        # edge case
        if matrix == []:
            return matrix

        # define your pointers in the matrix
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        ret = []
        while l < r and t < b:
            # top: add the top row to the list
            for i in range(l, r):
                ret.append(matrix[t][i])
            # right: add very right column to the list
            for i in range(t, b):
                ret.append(matrix[i][r])
            # bottom: add the very bottom row (from right to left)
            for i in range(r, l, -1):
                ret.append(matrix[b][i])
            # left: add the first column from the matrix
            for i in range(b, t, -1):
                ret.append(matrix[i][l])

        # restablish the pointers because we might still have missing values to add
            l += 1
            r -= 1
            t += 1
            b -= 1

        # single square in case the matrix is 3x3
        if l == r and t == b:
            ret.append(matrix[t][l])
        # vertical line in case your matrix is 4x4
        elif l == r:
            for i in range(t, b + 1):
                ret.append(matrix[i][l])
        # horizontal line in case your matrix is 4x4 or 4x3
        elif t == b:
            for i in range(l, r + 1):
                ret.append(matrix[t][i])
        return ret

def main():

    solution = Solution()
    res = solution.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(N) due to the list
'''