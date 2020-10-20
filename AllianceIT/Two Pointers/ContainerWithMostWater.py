"""
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
    are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
    forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    1. Create two pointers to that start at the beginning and at the end of the array.
    2. max_area will help us to determine the highest amount of water.
    3. min_p is the lowest bar from the array, we depend on the lowest bar because that makes the water not to overflow.
    4. Determine if the new calculated area > max_area and if so, then update the value of max_area
    5. if p1 <=2, then move the left bar to the right, otherwise move p2 to the left.
    6. Get the lowest bar from p1 and p2.

    Time complexity: O(n) and space O(1)
"""

def main():
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    result = solution.calculate_area(height)
    print(result)

class Solution:
    # def calculate_area_old(self, height):
    #     # create two pointers that indicate the start and end of the container
    #     p1, p2 = 0, len(height)-1
    #     # this will help us to determine the highest amount of water in the container
    #     max_area = 0
    #     # select the lowest pointer which represent a bar
    #     min_p = min(p1, p2)
    #     #area = 0
    #     for _ in height:
    #         print(height[p1:p2])
    #         area = (min_p*len(height[p1:p2]))
    #         area = p2-p1 * min(height[left], height[right])
    #         #print(area)
    #         if area > max_area:
    #             max_area = area
    #         if p1 <= p2:
    #             p1 += 1
    #         else:
    #             p2 -= 1
    #         min_p = min(p1,p2)
    #     return max_area

    def calculate_area(self, heights):
        # declare the two pointers that represent each bar
        left, right = 0, len(heights) - 1
        area = 0
        while left < right:
            # based on the lowest bar, you will multiply the distance from the right to left bar
            # (right-left) by the lowest bar in either side
            area = max(area, ((right - left) * min(heights[left], heights[right])))
            # if the left bar is lower than the right bar, increase it or move it to the right
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area

'''
    OPtimal solution
    
    class Solution:
    # @return an integer
    def maxArea(self, height):
        area, left, right = 0, 0, len(height) - 1
        
        while left < right:
            area = max(area, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area

'''


main()