'''
    Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
    If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell 
    (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and 
    they share an edge or a corner).

    The length of a clear path is the number of visited cells of this path.

    0 ->  0     0 
           \   
    1     1 ->  0
                |
                v
    1     1     0
    output: 4

    You can move up, down, left, right, 
    diagonal up-right, diagonal up-left, 
    diagonal down-left, diagonal down-right

    The difference with the treasure island is that we have 8 directions to move.
    total of 8 directions
    (curX, curY), dist = queue.popleft()
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
                        # x positions  # y positions   up-right down-right down-left up-left

    Another difference is that treasure island provides you an initial target whereas the 
    
    NOTICE: This only determines the path to go out from the grid, it won't help you to 
    
'''

from collections import deque

class Solution:
    def solve(self, grid):

        # we don't do a len(grid[0]) because this is a n*n matrix
        maxRow = maxCol = len(grid)-1

        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[maxRow][maxCol] != 0:
            return -1

        queue = deque()
        queue.append([(0,0), 1])
        # this is why we don't need a set to add the visited nodes, because we mark the nodes as visited
        grid[0][0] = 'V'

        while queue:
            (curX, curY), dist = queue.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
                        # x positions  # y positions   up-right down-right down-left up-left
            
            for direction in directions:
                newX = direction[0]+curX
                newY = direction[1]+curY
                
                # treasure found
                if self.validate(grid, newX, newY):
                    
                    if (newX,newY) == (maxRow, maxCol):
                        return dist + 1
                    
                    # safe pass
                    elif grid[newX][newY] == 0:
                        grid[newX][newY] = 1
                        queue.append([(newX, newY),dist+1])
        return -1

    def validate(self, grid, newX, newY):
        rows = len(grid)
        cols = len(grid[0])
        if newX < 0 or newY < 0 or newX >= rows or newY >= cols:
            return False
        return True

def main():
    grid = [[0,0,0,0,1],
            [1,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,1,0],
            [0,0,0,1,0]]
    solution = Solution()
    res = solution.solve(grid)
    print(res)

main()

'''
    Time complexity : O(N)
    Each cell was guaranteed to be enqueued at most once. 
    This is because a condition for a cell to be enqueued was that it had a zero in the grid, 
    and when enqueuing, we also permanently changed the cell's grid value to be non-zero.
    Space complexity: O(N)
    The only additional space we used was the queue. We determined above that at most, we enqueued N cells. 
    Therefore, an upper bound on the worst-case space complexity is O(N).
'''