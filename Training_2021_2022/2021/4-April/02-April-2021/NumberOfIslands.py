'''
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.

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
    islands = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col]=="1":
                dfs(grid, row, col)
                islands +=1
    return islands

def dfs(grid, row, col):

    # set the point as visited
    grid[row][col]="V"
    directions=[(1,0), (-1,0), (0,1), (0,-1)]
    for direction in directions:
        newXPosition = direction[0]+row
        newYPosition = direction[1]+col
        if validateGrid(grid, newXPosition, newYPosition) and grid[newXPosition][newYPosition]=="1":
            dfs(grid, newXPosition, newYPosition)


def validateGrid(grid, xPosition, yPosition):
    rows = len(grid)
    cols = len(grid[0])
    if xPosition<0 or yPosition <0 or xPosition>=rows or yPosition>=cols:
        return False
    return True


def main():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    res = solve(grid)
    print(res)

main()