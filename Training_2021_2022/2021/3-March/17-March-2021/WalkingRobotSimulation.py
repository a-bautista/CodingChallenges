'''
    A robot on an infinite XY-plane starts at point (0, 0) and faces north. 
    The robot can receive one of three possible types of commands:

        -2: turn left 90 degrees,
        -1: turn right 90 degrees, or
        1 <= k <= 9: move forward k units.

    Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi).

    If the robot would try to move onto them, the robot stays on the previous grid square instead 
    (but still continues following the rest of the route.)

    Return the maximum Euclidean distance that the robot will be from the origin squared 
    (i.e. if the distance is 5, return 25).

    Note:
        North means +Y direction.
        East means +X direction.
        South means -Y direction.
        West means -X direction.
'''

class Solution:
    def robotSimulation(self, commands, obstacles):
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = leftOrRight = 0
        # convert the obstacles into a set map, so we exclude this tuple when we encounter it
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:  #left
                leftOrRight = (leftOrRight - 1) % 4
            elif cmd == -1:  #right
                leftOrRight = (leftOrRight + 1) % 4
            else:
                for k in range(cmd):
                    # if you encounter the new computed move in the obstacleSet then avoid moving the robot
                    newX = x +dx[leftOrRight]
                    newY = y +dy[leftOrRight]
                    if (newX, newY) not in obstacleSet:
                        # accumulate the value in x or y
                        x += dx[leftOrRight]
                        y += dy[leftOrRight]
                        # Get the max distance by squaring the value of the x and y positions
                        ans = max(ans, x*x + y*y)
        return ans

def main():
    moves = [4, -1, 4, -2, 4]
    obstacles = [[2,4]]
    solution = Solution()
    res = solution.robotSimulation(moves, obstacles)
    print(res)

main()