'''
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
    horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

'''

def solve(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, grid, word):
                return True
    return False

def backtrack(row, col, grid, word):
    if len(word)==0:
        return True
    
    if row <0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col]!=word[0]:
        return False

    ret = False
    # mark the visited letter
    grid[row][col] = "#"
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for direction in directions:
        newXPos = direction[0] + row
        newYPos = direction[1] + col
        ret = backtrack(newXPos, newYPos, grid, word[1:])
        if ret:
            break
    
    # put back the letter as it was before
    grid[row][col] = word[0]

    return ret

def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    word2 = "SEE"
    word3 = "ABCD"
    #solution = Solution()
    res= solve(board, word)
    print(res)

main()