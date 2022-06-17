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
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    self.dfs(grid, x, y)
                    count+=1
        return count

    def dfs(self, grid, x, y):
        grid[x][y] = "V"
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if self.validate(grid, new_x, new_y) and grid[new_x][new_y]=="1":
                self.dfs(grid, new_x, new_y)

    def validate(self, grid, new_x, new_y):
        rows = len(grid)
        cols = len(grid[0])
        if new_x <0 or new_y < 0 or new_x >= rows or new_y >= cols:
            return False
        return True


def main():
    grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]

    solution = Solution()
    res = solution.solve(grid)
    print(res)

main()