'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
class Solution:
    def solve(self, grid):
        xRows = len(grid)
        yCols = len(grid[0])
        count = 0

        for x in range(xRows):
            for y in range(yCols):
                if grid[x][y]=="1":
                    self.dfs(grid, x, y)
                    count+=1
        return count

    # iterate over each point in the grid based in DFS, a for loop
    # declare DFS
    # set a new point of directions
    # move through that set of directions and call DFS
    # validate the results of the new point
    def dfs(self, grid, x, y):
        grid[x][y] = "V"
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for direction in directions:
            newPositionX = direction[0]+x
            newPositionY = direction[1]+y
            if self.validate(grid, newPositionX, newPositionY) and grid[newPositionX][newPositionY]=="1":
                self.dfs(grid, newPositionX, newPositionY)

    def validate(self, grid, newPositionX, newPositionY):
        xRows = len(grid)
        yCols = len(grid[0])
        if newPositionX < 0 or newPositionY < 0 or newPositionX>= xRows or newPositionY >= yCols:
            return False
        return True

def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    solution = Solution()
    res = solution.solve(grid)
    print(res)

main()

