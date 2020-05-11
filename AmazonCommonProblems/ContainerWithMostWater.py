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