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

def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "1":
                dfs(grid, x, y)
                count +=1
    return count
    
def dfs(grid, x, y):
    grid[x][y] = "V"
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for direction in directions:
        newPositionX = direction[0]+x
        newPositionY = direction[1]+y
        if validate(grid, newPositionX, newPositionY) and grid[newPositionX][newPositionY] == "1":
            dfs(grid, newPositionX, newPositionY)

def validate(grid, newPositionX, newPositionY):
    rows = len(grid)
    cols = len(grid[0])
    if newPositionX < 0 or newPositionY < 0 or newPositionY >= cols or newPositionX >= rows:
        return False
    return True


def main():
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    res = solve(grid)
    print(res)
    
main()