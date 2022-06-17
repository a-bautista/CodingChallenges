'''
    You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks 
    and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. 
    So you must figure out a shortest route to one of the treasure islands.

    Assume the map area is a two dimensional grid, represented by a matrix of characters. 
    You must start from one of the starting point (marked as S) of the map and can move one 
    block up, down, left or right at a time. The treasure island is marked as X. 
    Any block with dangerous rocks or reefs will be marked as D. 
    You must not enter dangerous blocks. You cannot leave the map area. 
    Other areas O are safe to sail in. 
    Output the minimum number of steps to get to any of the treasure islands.

    Example:

    Input:
    [['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O']]

    Output: 3
    Explanation:
    You can start from (0,0), (0, 3) or (0, 4). 
    The treasure locations are (2, 4) (3, 0) and (4, 0). 
    Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''

from collections import deque
class Solution:
    def shortestPath(self, grid):
        if not grid or not grid[0]:
            return 0
        
        res = float('inf')
        rows, cols = len(grid), len(grid[0])
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'S':
                    q = deque()
                    q.append([(row,col),0])
                    res = min(self.bfs(q, grid, rows, cols), res)       
        return res

    def bfs(self, queue, grid, row, col):
        # I cannot overwrite the matrix to indicate which nodes are visited, I need to create a new matrix
        # that sets the track
        visited = [[-1 for _ in range(col)]for _ in range(row)]
        while len(queue):
            (xPos, yPos), step = queue.popleft()
            visited[xPos][yPos] = step
            if grid[xPos][yPos] == 'X':
                return step
            
            for direction in self.directions:
                newX = direction[0]+xPos
                newY = direction[1]+yPos

                if newX >= 0 and newX < row and newY >= 0 and newY < col:
                    if grid[newX][newY] != 'D' and visited[newX][newY] == -1:
                        queue.append([(newX, newY), step+1])
        return -1

def main():
    grid = [['S', 'O', 'O', 'S', 'S'],
            ['D', 'O', 'D', 'O', 'D'],
            ['O', 'O', 'O', 'O', 'X'],
            ['X', 'D', 'D', 'O', 'O'],
            ['X', 'D', 'D', 'D', 'O']]
    solution = Solution()
    res = solution.shortestPath(grid)
    print(res)

main()