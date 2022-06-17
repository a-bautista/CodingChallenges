'''
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
    connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
    are surrounded by water.

    Count the number of distinct islands. An island is considered to be the same as another if and only if 
    one island can be translated (and not rotated or reflected) to equal the other.

    Example 1:

    11000
    11000
    00011
    00011

    Given the above grid map, return 1.

    Example 2:

    11011
    10000
    00001
    11011

    Given the above grid map, return 3.

    Notice that:

    11
    1

    and

    1
    11

    are considered different island shapes, because we do not consider reflection / rotation. 
    
'''

class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # edge cases
        if len(grid)==0 or len(grid[0])==0:
            return 0

        self.steps = ''
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.helper(grid, i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        return len(distinctIslands)
    
    def helper(self, grid, i, j, direct):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.steps += direct
            grid[i][j] = 0
            self.helper(grid, i+1, j, 'u')  # up 
            self.helper(grid, i-1, j, 'd')  # down
            self.helper(grid, i, j+1, 'r')  # right
            self.helper(grid, i, j-1, 'l')  # left
            self.steps += 'b'  # back
def main():
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    solution = Solution()
    res = solution.numDistinctIslands(grid)
    print(res)

main()

'''
    Time complexity: O(M*N) m rows and n columns and we need to touch every single element 
    Space complexity: O(M*N)
'''