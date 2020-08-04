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
        # def dfs(i, j):
        #     if not dp[i][j]:
        #         val = matrix[i][j]
        #         dp[i][j] = 1 + max(
        #             dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
        #             dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
        #             dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
        #             dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        #     return dp[i][j]
        #
        # if not matrix or not matrix[0]:
        #     return 0
        # M, N = len(matrix), len(matrix[0])
        # dp = [[0] * N for _ in range(M)]
        # #for x in range(M):
        # #    for y in range(N):
        # #        return max(dfs(x,y))
        # return max(dfs(x, y) for x in range(M) for y in range(N))

        # idea, use topological sort, search around to find the # of incoming nodes, start with zero indegree with queue, pop from queue, search around and reduce the indegree by 1; push to queue if indegree is 0. output the steps. Time O(mn) and Space O(mn).
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        hmap = {}
        queue = deque()
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m - 1 and 0 <= y <= n - 1 and matrix[x][y] < matrix[i][j]:
                        cnt += 1
                hmap[(i, j)] = cnt  # map point to the # of incoming degree
                if cnt == 0:
                    queue.append((i, j))  # append point (i,j) to queue
        # bfs with queue, and update the step until queue is empty
        step = 0
        while queue:
            size = len(queue)
            for k in range(size):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m - 1 and 0 <= y <= n - 1 and matrix[x][y] > matrix[i][j] and (x, y) in hmap:
                        hmap[(x, y)] -= 1
                        if hmap[(x, y)] == 0:
                            queue.append((x, y))
            step += 1
        return step


def main():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    solution = Solution()
    res = solution.longestIncreasingPath(matrix)
    print(res)


main()