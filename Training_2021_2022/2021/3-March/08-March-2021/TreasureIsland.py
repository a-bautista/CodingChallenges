'''
   You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
   Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest
   route to the treasure island. Assume the map area is a two dimensional grid, represented by a matrix of characters.
   You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
   The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
   Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
   You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
   Output the minimum number of steps to get to the treasure.

   'O', 'O', 'O', 'O'
   'D', 'O', 'D', 'O'
   'O', 'O', 'O', 'O'
   'X', 'D', 'D', 'O'
'''
from collections import deque

class Solution:
    def solve(self, grid):
        # edge cases: 
        # no x or y
        queue = deque()
        queue.append([(0,0),0])
        grid[0][0] = 'V'

        while queue:
            (currentPositionX, currentPositionY), steps = queue.popleft()
            directions = [(1,0),(-1,0), (0,1), (0,-1)]
            for direction in directions:
                newPositionX = currentPositionX + direction[0]
                newPositionY = currentPositionY + direction[1]

                if self.validate(grid, newPositionX, newPositionY):
                    if (grid[newPositionX][newPositionY] == 'X'):
                        return steps + 1
                    if (grid[newPositionX][newPositionY] == 'O'):
                        # mark the node as visited
                        grid[newPositionX][newPositionY] = "V"
                        queue.append([(newPositionX, newPositionY), steps + 1])

    # I need to check if the current position is valid 
    def validate(self, grid, newX, newY):
        xRows = len(grid)
        yCols = len(grid[0])
        if newX < 0 or newY < 0 or newX >= xRows or newY >= yCols:
            return False        
        return True


def main():
    grid = [ ['O', 'O', 'O', 'O'],
             ['D', 'O', 'D', 'O'],
             ['O', 'O', 'O', 'O'],
             ['X', 'D', 'D', 'O']]
    solution = Solution()
    res = solution.solve(grid)
    print(res)

main()