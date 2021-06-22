from collections import deque

class Solution:
    def solution(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return -1  # impossible

        # tuple of tuples in a double ended queue contained in a list
        # you can add elements to the right (q.append()) or to the left (q.appendleft())
        q = deque([((0, 0), 0)])  # ((x, y), step)
        # mark the first node as visited
        matrix[0][0] = "V"
        while q:
            # set the values to (0,0), 0 and make the double ended queue empty,
            # so when you find an incorrect path then the steps that were used will be deleted
            (x, y), step = q.popleft()

            print((x, y), step)

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                if self.validateMatrix(x, y, direction, matrix):
                    if matrix[x + direction[0]][y + direction[1]] == "X":
                        print('Treasure found!')
                        return step + 1
                    if matrix[x + direction[0]][y + direction[1]] == "O":
                        # mark the matrix as visited
                        matrix[x + direction[0]][y + direction[1]] = "V"

                        # append the visited node to the queue,
                        q.append(((x + direction[0], y + direction[1]), step + 1))
                        print(q)
        return -1


    def validateMatrix(self, x, y, direction, matrix):
        # get the total rows # and total columns
        nrow, ncol = len(matrix), len(matrix[0])
        if 0 <= x + direction[0] < nrow and 0 <= y + direction[1] < ncol:
            return True
        return False

if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'],
                    ['D', 'O', 'D', 'O'],
                    ['O', 'O', 'O', 'O'],
                    ['X', 'D', 'D', '0']]

    solution = Solution()
    res = solution.solution(treasure_map)
    print("Result: ", res)

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