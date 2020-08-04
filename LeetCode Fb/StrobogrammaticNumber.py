'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.



Example 1:

Input: num = "69"
Output: true

Example 2:

Input: num = "88"
Output: true


'''


class Solution(object):
    def isStrobogrammatic(self, s):

        if not s:
            return False

        pairs = set([('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')])
        l, r = 0, len(s) - 1

        while l <= r:
            if (s[l], s[r]) not in pairs:
                return False
            l += 1
            r -= 1
        return True

'''
    Time complexity: O(N)
    
'''

