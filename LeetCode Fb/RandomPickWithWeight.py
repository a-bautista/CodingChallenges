from random import random
class Solution:
    def __init__(self, w):
        '''
            Generate the cumulative sums array.
        '''
        self.prefix_sums =[]
        self.sum = 0

        for weight in w:
            self.sum += weight
            self.prefix_sums.append(self.sum)
        self.total = self.sum

    def pickIndex(self):

        left, right = 0, len(self.prefix_sums) - 1
        target = self.total * random()

        while left < right:
            mid = left + (right - left)//2
            if target < self.prefix_sums[mid]:
                right = mid
            else:
                left = mid + 1
        return left




'''
    Time complexity: Log(N)
    Space complexity: O(N) for the init and O(1) for pickIndex.
'''