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
        x_move = len(grid)
        y_move = len(grid[0])
        count = 0
        for x in range(x_move):
            for y in range(y_move):
                if grid[x][y] == 1:
                    self.dfs(grid, x, y)
                    count+=1
        return count

    def dfs(self, grid, x, y):
        grid[x][y] = 'X'
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        #directions = [(0,1), (0,-1),(1,0), (-1, 0)]

        for direction in directions:
            new_x_move = x + direction[0]
            new_y_move = y + direction[1]
            # validate if the new move you want to attempt is valid before looking for the value 1 in the grid
            if self.validate(grid, new_x_move, new_y_move) and grid[new_x_move][new_y_move] == 1:
                self.dfs(grid, new_x_move, new_y_move)

    def validate(self, grid, new_x, new_y):
        x = len(grid)
        y = len(grid[0])

        if new_x<0 or new_y <0 or new_x >= x or new_y >= y:
            return False
        return True


def main():
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]

    grid2 = [[1, 1, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 0]]

    solution = Solution()
    res = solution.solve(grid2)
    print(res)

main()