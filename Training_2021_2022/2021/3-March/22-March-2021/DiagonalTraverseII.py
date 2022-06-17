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
'''
from collections import deque
def solve(matrix):
    rows = len(matrix)
    queue = deque()
    queue.append((0,0))
    res = []

    while queue:
        currentX, currentY = queue.popleft()
        res.append(matrix[currentX][currentY])
        if currentY == 0 and currentX + 1 < rows:
            queue.append((currentX + 1, currentY))
        
        if currentY + 1 < len(matrix[currentX]):
            queue.append((currentX, currentY + 1))

    return res


def main():
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    res = solve(nums)
    print(res)

main()
    