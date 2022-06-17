'''
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
    horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

'''
# class Solution:
#     # def __init__(self):
#     #     #self.bucket = len()
#     #     self.i = 0

#     def solve(self, grid, str1):
#         rows = len(grid)
#         cols = len(grid[0])
#         i =0
#         bucket = len(str1)-1
#         #visited = set()

#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == str1[i]:
#                     # the variables need to be protected when you traverse in DFS
#                     i+=1
#                     bucket-=1
#                     boolVal = self.dfs(grid, row, col, str1, i, bucket)
#                     # backtrack?
#                     if not boolVal:
#                         i-=1
#                         bucket+=1

#         if bucket == 0 and i==len(str1)-1:
#             return True
#         else:
#             return False


#     def dfs(self, grid, row, col, str1, i, bucket):
#         #visited.add(grid[row][col])
#         #i+=1
#         #bucket-=1
#         directions = [(0,1), (0,-1), (1,0), (-1,0)]
#         for direction in directions:
#             newX = direction[0] + row
#             newY = direction[1] + col

#             if self.validate(grid, newX, newY) and bucket>=0 and grid[newX][newY] == str1[i]:
#                 # the variables need to be protected when you traverse in DFS
#                 i+=1
#                 bucket-=1
#                 self.dfs(grid, newX, newY, str1, i, bucket, visited)
#                 return True
#         return False

#     def validate(self, grid, newX, newY):
#         rows = len(grid)
#         cols = len(grid[0])
#         if newX < 0 or newY < 0 or newX >= rows or newY >= cols:
#             return False
#         return True

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        
        # explore the 4 neighbor directions
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for direction in directions:
            newX = direction[0]+row
            newY = direction[1]+col
            # if self.validate(newX, newY) or self.board[row][col] != suffix[0]:
            #     ret = True
            ret = self.backtrack(newX, newY, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: 
                break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret

    # def validate(self, newX, newY):
        
    #     if newX <0 or newY < 0 or newX>= self.ROWS or newY >= self.COLS:
    #         return False
    #     return True


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    word2 = "SEE"
    word3 = "ABCD"
    solution = Solution()
    res= solution.exist(board, word3)
    print(res)

main()