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
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        left = 0
        right = len(height)-1
        while left < right:
            #If left pointer is smaller than right pointer, then the trapped water depends on the
            # left pointer
            if height[left] < height[right]:
                # if the current left pointer is greater than the max left pointer
                if height[left] > max_l:
                    # update left max
                    max_l = height[left]
                else:
                    # start capturing water only when we have the left max available
                    # water goes from left max bar to the lower left bar
                    areas += max_l - height[left]
                # sum 1, move to the right
                left +=1
            # the left pointer is greater than the right pointer, then the trapped water depends
            # on the right pointer
            else:
                if height[right] > max_r:
                    max_r = height[right]
                else:
                    # start capturing water only when we have the right max available
                    # water goes right max bar to the lower right bar
                    areas += max_r - height[right]
                # subtract 1, move to the left
                right -=1
        return areas

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''