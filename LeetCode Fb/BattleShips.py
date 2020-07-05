from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        x_columns = len(board)
        y_columns = len(board[0])
        for row in range(x_columns):
            for col in range(y_columns):
                if board[row][col] == 'X':
                    flag = 1
                    # check if there's a battleship to the left
                    if col >0 and board[row][col-1] == 'X':
                        flag = 0
                    # check if there's a battleship to the up
                    if row > 0 and board[row-1][col] == 'X':
                        flag = 0
                    total += flag
        return total


'''
    Time complexity: O(n**2) because we depend on the number of rows and columns
    Space complexity: O(1)

'''
