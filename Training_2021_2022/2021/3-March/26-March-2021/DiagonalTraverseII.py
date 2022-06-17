'''
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

    Input: nums = [[1,2,3],[4,5,6],[7,8,9]]

        [1,2,3]
        [4,5,6]
        [7,8,9]

    Elements are all up in the diagonal.
    Output: [1,4,2,7,5,3,8,6,9]
    Same analogy applies to all nodes nums[i][j]
    This can be solved in a BFS fashion because we can attach the left and right child of the matrix in a queue.

        1->2 and 4
        2->5 and 3

'''
from collections import deque
def solve(matrix):
    queue = deque()
    queue.append((0,0)) # get the positions 
    res = []
    while queue:
        # get the positions of the grid
        currentX, currentY = queue.popleft()
        res.append(matrix[currentX][currentY])
        
        # hold the position Y to 0 because we need to get first the child elements of the top most left column
        if currentY == 0 and currentX + 1 < len(matrix[0]):
            # move the x pointer to the next row
            queue.append((currentX+1, currentY))

        if currentY + 1 < len(matrix[0]):
            # move the y column to the next col
            queue.append((currentX, currentY+1))

    return res

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = solve(matrix)
    print(res)

main()