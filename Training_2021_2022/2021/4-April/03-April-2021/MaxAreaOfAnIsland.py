'''
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
    connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are 
    surrounded by water.

    Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

    Example 1:

    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    Given the above grid, return 6. Note the answer is not 11, because the island must be 
    connected 4-directionally.

    Example 2:

    [[0,0,0,0,0,0,0,0]]

    Given the above grid, return 0. 

'''
class Solution:
    def solve(self, grid):
        count =0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    count = max(count, self.dfs(row, col, grid))
        return count

    def dfs(self, x, y, grid):
        if x >= len(grid) or y >= len(grid[0]) or x <0 or y <0 or grid[x][y]==0:
            return 0

        grid[x][y]=0
        up = self.dfs(x+1, y, grid)
        down = self.dfs(x-1, y, grid)
        left = self.dfs(x, y-1, grid)
        right = self.dfs(x, y+1, grid)
        return up + down + left + right + 1


def main():
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    solution = Solution()
    res = solution.solve(grid)
    print(res)

main()