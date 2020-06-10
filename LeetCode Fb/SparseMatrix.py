"""
    Given two sparse matrices A and B, return the result of AB.
    You may assume that A's column number is equal to B's row number
    (so, in this case it will be possible to multiply the matrices).

    A =
    [
        [1, 1, 0],
        [-1,0, 3]
    ]
    2 * 3
    rows * columns
    B =
    [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    3 * 3
    rows * columns

"""

class Solution:
    def multiply(self, A, B):
        if A is None or B is None:
            return None

        rowsA, columnsA = len(A), len(A[0]) # get the rows and columns
        rowsB, columnsB = len(B), len(B[0])

        if rowsB != columnsA:
            raise Exception("It is not possible to do the multiplication because A's columns"
                            "have not the same size as B's rows.")

        tableA, tableB = dict(), dict()

        # We need to create 2 tables to make this memory efficient
        # the tables are used to locate the non zero values
        for row, column in enumerate(A):

            for col_index, col_element in enumerate(column):
                # if col_element is not 0
                if col_element:

                    if row not in tableA:

                        tableA[row] = dict()

                    tableA[row][col_index] = col_element


        for row, column in enumerate(B):
            for col_index, col_element in enumerate(column):
                if col_element:
                    if row not in tableB:
                        tableB[row] = dict()
                    tableB[row][col_index] = col_element

        # create a matrix of zeroes to store the values and will be used to store the results
        c = [[0 for _ in range(columnsB)] for _ in range(rowsA)]

        # do the operations to resolve
        for i in tableA:
            for k in tableA[i]:
                if k not in tableB:
                    continue
                for j in tableB[k]:
                    c[i][j] += tableA[i][k] * tableB[k][j]
        return c

# class Solution(object):
#     def multiply(self, A, B):
#         """
#         :type A: List[List[int]]
#         :type B: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if A is None or B is None: return None
#         m, n, l = len(A), len(A[0]), len(B[0])
#         if len(B) != n:
#             raise Exception("A's column number must be equal to B's row number.")
#         C = [[0 for _ in range(l)] for _ in range(m)]
#         tableB = {}
#         for k, row in enumerate(B):
#             tableB[k] = {}
#             for j, eleB in enumerate(row):
#                 if eleB: tableB[k][j] = eleB
#         for i, row in enumerate(A):
#             for k, eleA in enumerate(row):
#                 if eleA:
#                     for j, eleB in tableB[k].iteritems():
#                         C[i][j] += eleA * eleB
#         return C

# class Solution(object):
#     def multiply(self, A, B):
#         """
#         :type A: List[List[int]]
#         :type B: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if len(A) == 0 or len(B) == 0:
#             return [[]]
#
#         a, c, b = len(A), len(B), len(B[0])
#         AB = [[0 for _ in range(b)] for _ in range(a)]
#
#         for i in range(a):
#             for j in range(c):
#                 if A[i][j] != 0:
#                     for k in range(b):
#                         if B[j][k] != 0:
#                             AB[i][k] += A[i][j] * B[j][k]
#         return AB


def main():
    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]

    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    solution = Solution()
    res = solution.multiply(A,B)
    print(res)


main()