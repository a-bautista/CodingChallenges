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
def solve(matrix):

    # 1. Value in rows and columns contain the elements in traversal order.
    # 2. Reverse only the even values from rows and columns.

    rows_len = len(matrix)
    cols_len = len(matrix[0])
    dd = defaultdict(list)
    res = []

    # 1. Elements in traversal order
    for rows in range(rows_len):
        for cols in range(cols_len):
            dd[rows+cols].append(matrix[rows][cols])

    # 2. Reverse only the even values
    for i in range(rows_len + cols_len - 1):
        if i % 2 == 0:
            res.append(dd[i][::-1])
        else:
            res.append(dd[i])

    return res


def main():

    matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    res = solve(matrix)
    print(res)

main()
