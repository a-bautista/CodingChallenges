class Solution(object):
    def numIslandsDFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        mrows, ncolumns = len(grid), len(grid[0])
        count = 0
        for i in range(mrows):
            for j in range(ncolumns):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, column):
        grid[row][column] = 'X'
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for direction in directions:
            nrow, ncolumn = row + direction[0], column + direction[1]
            if self.is_valid(grid, nrow, ncolumn) and grid[nrow][ncolumn] == '1':
                self.dfs(grid, nrow, ncolumn)

    def is_valid(self, grid, row, column):
        m, n = len(grid), len(grid[0])
        if row < 0 or column < 0 or row >= m or column >= n:
            return False
        return True

def main():
    l = [
         ["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]
    ]

    solution = Solution()
    res = solution.numIslandsDFS(l)
    print(res)

main()

'''
    Time complexity: O(M*N)
    Space complexity: O(M*N)
'''