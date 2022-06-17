'''
   You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
   Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest
   route to the treasure island. Assume the map area is a two dimensional grid, represented by a matrix of characters.
   You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
   The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
   Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
   You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
   Output the minimum number of steps to get to the treasure.

   'O', 'O', 'O', 'O'
   'D', 'O', 'D', 'O'
   'O', 'O', 'O', 'O'
   'X', 'D', 'D', 'O'
'''
from collections import deque
class Solution:
    def solve(self, matrix):
        x_rows = len(matrix)
        y_cols = len(matrix[0])
        if x_rows == 0 or y_cols ==0:
            return -1

        queue = deque()
        queue.append([(0,0),0])
        matrix[0][0] = "V"

        while queue:
            (x,y), steps = queue.popleft()
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]

                if self.validate(matrix, new_x, new_y):
                    if matrix[new_x][new_y] == "X":
                        # treasure was found
                        return steps + 1
                    if matrix[new_x][new_y] == "O":
                        matrix[new_x][new_y] = "V"
                        queue.append([(new_x, new_y),steps + 1])

    def validate(self, grid, new_x, new_y):
        x_len = len(grid)
        y_len = len(grid[0])
        if new_x < 0 or new_y < 0 or new_x >= x_len or new_y >= y_len:
            return False
        return True


def main():
    treasure_map = [['O', 'O', 'O', 'O'],
                    ['D', 'O', 'D', 'O'],
                    ['O', 'O', 'O', 'O'],
                    ['O', 'D', 'D', 'X']]
    solution = Solution()
    res = solution.solve(treasure_map)
    print("Result: ", res)

main()
