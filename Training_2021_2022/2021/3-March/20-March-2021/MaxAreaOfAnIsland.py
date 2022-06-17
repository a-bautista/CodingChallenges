# def solve(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     count = 0
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x][y] == 1:
#                 count = max(dfs(grid, x, y), count)
#     return count
#
# def dfs(grid, i, j):
#     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
#         return 0
#
#     grid[i][j] = 0
#
#     up = dfs(i, j + 1, grid)
#     down = dfs(i, j - 1, grid)
#     left = dfs(i - 1, j, grid)
#     right = dfs(i + 1, j, grid)
#
#     return up + down + left + right + 1
#
#     # grid[x][y] = -1
#     # directions = [(0,1),(0,-1),(1,0),(-1,0)]
#     # for direction in directions:
#     #     newPositionX = direction[0]+x
#     #     newPositionY = direction[1]+y
#     #     if validate(grid, newPositionX, newPositionY) and grid[newPositionX][newPositionY] == 1:
#     #         value = dfs(grid, newPositionX, newPositionY)
#     #         return value + 1
#
# def validate(grid, x, y):
#     rows = len(grid)
#     cols = len(grid[0])
#     if x < 0 or y < 0 or x >= rows or y >= cols:
#         return False
#     return True
#
# def main():
#     grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
#     res = solve(grid)
#     print(res)
#
# main()

'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = max(self.dfs(i, j, grid), count)
        return count

    def dfs(self, i, j, grid):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0


        up = self.dfs(i, j + 1, grid)
        down = self.dfs(i, j - 1, grid)
        left = self.dfs(i - 1, j, grid)
        right = self.dfs(i + 1, j, grid)

        return up + down + left + right + 1


def main():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    solution = Solution()
    res = solution.maxAreaOfIsland(grid)
    #res = solve(grid)
    print(res)

main()