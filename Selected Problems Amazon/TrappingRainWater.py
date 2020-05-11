"""
    O(N) time
    O(1) space
    We can use two pointers.


    Initialize left pointer to 0 and right pointer to size-1
    While left<right do:
        If height[left] is smaller than height[right] (pointer left is smaller than right)
            If height[left]≥left_max,
                update left_max
            Else
                add areas = left_max − height
            Add 1 to left so you can move to the right
        Else
            If height[right]≥right_max
                update max_right
            Else
                add areas = right_max−height[right]
            Subtract 1 from right so you can move to the left


"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -=1
        return areas