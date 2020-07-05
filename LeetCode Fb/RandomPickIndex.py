from random import randint

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):

        res = -1
        count =0

        for i, x in enumerate(self.nums):
            if target == x:
                count += 1
                chance = randint(1, count)
                if count == chance:
                    # in case you are given an array with different numbers
                    # then just return the index of that character when it appeared
                    res = i
        return res


    '''
        Time complexity: O(n) where n is the size of the array of numbers
        Space complexity: O(k) where k is the number of times the target appeared
    '''