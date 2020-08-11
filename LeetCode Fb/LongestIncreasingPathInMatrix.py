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

from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix):
        # corner case
        if not matrix or not matrix[0]:
            return 0

        # initialization
        M, N = len(matrix), len(matrix[0])  # length, width
        dp = [[0] * N for i in range(M)]  # 2-D matrix for store the number of steps

        # dfs function
        def dfs(i, j):
            if not dp[i][j]:  # if this position is not visited
                val = matrix[i][j]
                # search four directions to find out the decreasing path
                # up
                if i and val > matrix[i - 1][j]:
                    up = dfs(i - 1, j)
                else:
                    up = 0
                # down
                if i < M - 1 and val > matrix[i + 1][j]:
                    down = dfs(i + 1, j)
                else:
                    down = 0
                # left
                if j and val > matrix[i][j - 1]:
                    left = dfs(i, j - 1)
                else:
                    left = 0
                # right
                if j < N - 1 and val > matrix[i][j + 1]:
                    right = dfs(i, j + 1)
                else:
                    right = 0
                # "walk" to the target neighbor and accumulate the number of steps
                dp[i][j] = 1 + max(up, down, left, right)
            return dp[i][j]

        res_path = []
        for x in range(M):  # search the grid by dfs
            for y in range(N):
                res_path.append(dfs(x, y))

        return max(res_path)


def main():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    solution = Solution()
    res = solution.longestIncreasingPath(matrix)
    print(res)


main()