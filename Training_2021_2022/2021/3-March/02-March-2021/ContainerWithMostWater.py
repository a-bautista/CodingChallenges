'''
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
    are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
    forms a container, such that the container contains the most water.

 5  |                      |
 4  |     |     |          |
 3  |     |     |          |
 2  |     |     |    |     |
 1  |     |     |    |     |
    |_____|_____|____|_____|___
   a1    a2    a3    a4   a5

    Note: You may not slant the container and n is at least 2.

    1. Create two pointers to that start at the beginning and at the end of the array.
    2. max_area will help us to determine the highest amount of water.
    3. min_p is the lowest bar from the array, we depend on the lowest bar because that makes the water not to overflow.
    4. Determine if the new calculated area > max_area and if so, then update the value of max_area
    5. if p1 <=2, then move the left bar to the right, otherwise move p2 to the left.
    6. Get the lowest bar from p1 and p2

    Time complexity: O(n) and space O(1)
'''

def solve(nums):
    left, right = 0,len(nums)-1
    water = 0
    while left < right:
        water =max(water, ((right - left) * min(nums[left], nums[right])))

        if nums[left] <nums[right]:
            left +=1
        else:
            right -=1
    return water

def main():
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = solve(nums)
    print(res)

main()