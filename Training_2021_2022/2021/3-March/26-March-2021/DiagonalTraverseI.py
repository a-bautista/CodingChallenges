"""
    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal 
    order as shown in the below image.

    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]

    [1,2,4,7,5,3,6,8,9]
    
    The trick is that rows and columns have the same number, i.e.,
    
    [
          0  1  2
      0 [ 1, 2, 3 ],
      1 [ 4, 5, 6 ],
      2 [ 7, 8, 9 ]
    ]
    
    You need a defaultdict to store this a key, value pair. 
     0     1       2       3      4
    [1]  [2,4]  [3,5,7]   [6,8]  [9]

    I need to append the results in a list, then I need to invert the even numbered arrays

    O(1) adding to an array
    O(n*log*n) for sorting the array
"""
from collections import defaultdict
import itertools

def solve(matrix):
    general = []
    rows = len(matrix) # O(1) in time
    cols = len(matrix[0])
    dd = defaultdict(list)


    # store the values in a defaultdict
    for row in range(rows):
        for col in range(cols):
            dd[row+col].append(matrix[row][col])
    
    # reverse the even key values O(n*log(n))
    for key, val in dd.items():
        if key%2==0:
            general.append(val[::-1])
        else:
            general.append(val)

    # compress the list of lists to just 1 list
    return list(itertools.chain(*general))


def main():
    matrix = [[ 1, 2, 3 ], [ 4, 5, 6 ],[ 7, 8, 9 ]]
    res = solve(matrix)
    print(res)

main()