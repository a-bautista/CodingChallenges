'''
You are given an m x n grid rooms initialized with these three possible values.

    -1  A wall or an obstacle.
     0  A gate.
    INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance
    to a gate is less than 2147483647.

    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''

from collections import deque
class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        # if rooms are empty then return null
        if not rooms:
            return None

        x_rows, y_cols = len(rooms), len(rooms[0])
        queue = deque()

        # add all the gates to the queue (each element in the queue is in the x,y coordinate format)
        for x in range(x_rows):
            for y in range(y_cols):
                if rooms[x][y] == 0:
                    queue.append((x, y))

        distance = 0
        # generate the directions for moving in the matrix
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            length = len(queue)
            # increase the distance every time you add a new element to the queue
            distance += 1
            for _ in range(length):
                current_room = queue.popleft()
                for direction in directions:
                    x_pos = current_room[0] + direction[0]
                    y_pos = current_room[1] + direction[1]

                    if self.validate(rooms, x_pos, y_pos) and rooms[x_pos][y_pos] == 2147483647: # empty room
                        # update the matrix with the distance to the gate
                        rooms[x_pos][y_pos] = distance
                        queue.append([x_pos, y_pos])

        return rooms

    def validate(self, grid, new_x, new_y):
        x_rows = len(grid)
        y_cols = len(grid[0])
        if new_x < 0 or new_y < 0 or new_x >= x_rows or new_y >= y_cols:
            return False
        return True

def main():
    rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
    solution = Solution()
    res = solution.wallsAndGates(rooms)
    print(res)

main()