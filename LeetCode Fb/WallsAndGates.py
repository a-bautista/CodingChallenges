from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # if rooms are empty then return null
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # generate the directions for moving in the matrix
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        # add all the gates to the queue (each element in the queue is in the x,y coordinate format)
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        distance = 0
        while queue:
            length = len(queue)
            # increase the distance every time you add a new element to the queue
            distance += 1
            for i in range(length):
                cur = queue.popleft()
                for dir in dirs:
                    nextPos = (cur[0]+dir[0], cur[1]+dir[1])
                    if nextPos[0] >= 0 and nextPos[0] < m and nextPos[1] >= 0 and nextPos[1] < n and rooms[nextPos[0]][nextPos[1]] == 2147483647:
                        # update the matrix with the distance to the gate
                        rooms[nextPos[0]][nextPos[1]] = distance
                        queue.append(nextPos)

'''
    Time complexity: O(M*n)
    Space complexity: O(M*n)
'''