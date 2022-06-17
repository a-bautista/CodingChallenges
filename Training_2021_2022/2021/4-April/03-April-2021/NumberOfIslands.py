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
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    self.dfs(grid, row, col)
                    count +=1
        return count

    def dfs(self, grid, row, col):
        grid[row][col] = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            newXPosition = direction[0]+row
            newYPosition = direction[1]+col
            if self.validate(grid, newXPosition, newYPosition) and grid[newXPosition][newYPosition]=="1":
                self.dfs(grid, newXPosition, newYPosition)
                
    def validate(self, grid, newXPosition, newYPosition):
        rows = len(grid)
        cols = len(grid[0])
        if newXPosition<0 or newYPosition < 0 or newXPosition>=rows or newYPosition>=cols:
            return False
        return True
            