'''

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

    You receive a valid board, made of only battleships or empty slots.
    Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
    At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:

X..X
...X
...X

In the above board there are 2 battleships.

Invalid Example:

...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

Basically we need to check if we have adjacent battleships (to the left and up). If we have adjacent battleships
then we don't count them.

'''

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
    Time complexity: O(m*n) because we depend on the number of rows and columns
    Space complexity: O(1)

'''
