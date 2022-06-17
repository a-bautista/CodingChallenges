'''
    We are given an array asteroids of integers representing asteroids in a row.
    For each asteroid, the absolute value represents its size, and the sign represents its direction 
    (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
    If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

    Example 1:

    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

    Example 2:

    Input: asteroids = [8,-8]
    Output: []
    Explanation: The 8 and -8 collide exploding each other.
'''

def solve(asteroids):

    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        
        # negative values
        else:
            # if we have elements in the stack and the last element in the stack is 
            # positive and the last element of the stack is less than the current asteroid then
            # this new asteroid will destroy the last element in the stack because it has a greater value
            while stack and stack[-1]>0 and stack[-1]<abs(asteroid):
                stack.pop()
            if not stack or stack[-1]<0:
                stack.append(asteroid)
            # -8,8,-8,8 = -8, 8
            elif stack[-1]==-asteroid:
                stack.pop()
    return stack

def main():
    asteroids = [-8,8,-8,8]
    res = solve(asteroids)
    print(res)

main()
    