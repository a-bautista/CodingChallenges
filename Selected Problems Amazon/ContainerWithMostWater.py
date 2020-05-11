"""
    1. Create two pointers to that start at the beginning and at the end of the array.
    2. max_area will help us to determine the highest amount of water.
    3. min_p is the lowest bar from the array, we depend on the lowest bar because that makes the water not to overflow.
    4. Determine if the new calculated area > max_area and if so, then update the value
    5. if p1 <=2, then move the left bar to the right, otherwise move p2 to the left.
    6. Get the lowest bar from p1 and p2

    Time complexity: O(n) and space O(1)

"""

def main():
    height = [1,8,6,2,5,4,8,3,7]
    result = Solution.calculate_area(Solution,height)
    print(result)

class Solution:
    def calculate_area(self, height):
        p1, p2 = 0, len(height)-1
        max_area = 0
        min_p = min(p1,p2)
        #area = 0
        for _ in height:
            area = (min_p*height[p1:p2-1])
            if area > max_area:
                max_area = area
            if p1 <= p2:
                p1 += 1
            else:
                p2 -= 1
            min_p = min(p1,p2)
        return max_area

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