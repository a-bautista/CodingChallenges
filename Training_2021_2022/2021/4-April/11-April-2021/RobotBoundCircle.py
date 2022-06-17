'''
    On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of
    three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degrees to the right.

    The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

    Input: instructions = "GGLLGG"
    Output: true
    
    Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
'''

def solve(instructions):
    # r = right, u = up, l = left, d = down
    #    r   u   l  d 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, 1]
    x = y = 0
    idx = 0 # facing north
    for i in instructions:
        # move to the left
        if i == "L":
            idx = (idx - 1) % 4
        elif i == "R":
            idx = (idx + 1) % 4
        else:
            x+= dx[idx]
            y+= dy[idx]
    
    return (x==0 and y==0) or idx!=0

def main():
    instructions = "GL"
    res = solve(instructions)
    print(res)

main()

