'''
    Given an integer matrix, find the length of the longest increasing path.

    From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

    Example 1:

    Input: nums =
    [
    [9,9,4],
    [6,6,8],
    [2,1,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

    Example 2:

    Input: nums =
    [
    [3,4,5],
    [3,2,6],
    [2,2,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

'''

# def solve(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     resPath = []

#     for row in range(rows):
#         for col in range(cols):
#             resPath.append(dfs(row, col))


# def dfs():
#     pass


# def main():
#     matrix = [[9,9,4], [6,6,8], [2,1,1]]


# main()


'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


'''

class Solution:
    # def validate(self, grid, newX, newY):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     if newX > grid[rows][cols]

    def longestIncreasingPath(self, matrix):
        # corner case
        if not matrix or not matrix[0]:
            return 0

        # initialization
        rows, cols = len(matrix), len(matrix[0])  # length, width
        dp = [[0] * N for i in range(rows)]  # 2-D matrix for store the number of steps

        # dfs function
        def dfs(x, y):
            if not dp[x][y]:  # if this position is not visited
                val = matrix[x][y]
                # directions = [(0,1),(0,-1), (1,0), (-1,0)]
                # for direction in directions:
                #     newX = direction[0]+i
                #     newY = direction[1]+j

                # search four directions to find out the decreasing path
                # up
                if x and val > matrix[x - 1][y]:
                    up = dfs(x - 1, y)
                else:
                    up = 0
                # down
                if x < rows - 1 and val > matrix[x + 1][y]:
                    down = dfs(x + 1, y)
                else:
                    down = 0
                # left
                if y and val > matrix[x][y - 1]:
                    left = dfs(x, y - 1)
                else:
                    left = 0
                # right
                if y < cols - 1 and val > matrix[x][y + 1]:
                    right = dfs(x, y + 1)
                else:
                    right = 0
                # "walk" to the target neighbor and accumulate the number of steps
                dp[x][y] = 1 + max(up, down, left, right)
            return dp[x][y]

        res_path = []
        for x in range(rows):  # search the grid by dfs
            for y in range(cols):
                res_path.append(dfs(x, y))
        return max(res_path)


def main():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    solution = Solution()
    res = solution.longestIncreasingPath(matrix)
    print(res)


main()