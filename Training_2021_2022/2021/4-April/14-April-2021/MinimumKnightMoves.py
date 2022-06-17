'''
    In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
    A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal 
    direction, then one square in an orthogonal direction.

    Return the minimum number of steps needed to move the knight to the square [x, y].  
    It is guaranteed the answer exists.

    Example 1:

    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

    Example 2:

    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

'''
from collections import deque
class Solution:
    def minKnightMoves(self, x, y):
        # declare the directions from where to move
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        # start adding the initial position
        queue = deque([(0, 0)])

        seen = set()
        seen.add((0, 0))

        x = abs(x)
        y = abs(y)
        steps = 0

        # bfs
        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()

                # you found the target coordinate
                if cur_x == x and cur_y == y:
                    return steps

                # move into the different directions
                for d in directions:
                    new_x = cur_x + d[0]
                    new_y = cur_y + d[1]
                    
                    # the -2 indicates that you are navigating in the allowed boundaries of the quadrant
                    if (new_x, new_y) not in seen and -2 <= new_x <= x + 2 and -2 <= new_y <= y + 2:
                        queue.append((new_x, new_y))
                        seen.add((new_x, new_y))
            steps += 1
        return steps

def main():
    target_x = 5
    target_y = 5
    solution = Solution()
    res = solution.minKnightMoves(target_x, target_y)
    print(res)

main()
