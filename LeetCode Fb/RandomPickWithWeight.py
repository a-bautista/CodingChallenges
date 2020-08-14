'''
Given an array w of positive integers, where w[i] describes the weight of index i(0-indexed), write a function pickIndex
which randomly picks an index in proportion to its weight.

For example, given an input list of values w = [2, 8], when we pick up a number out of it, the chance is that 8 times out
of 10 we should pick the number 1 as the answer since it's the second element of the array (w[1] = 8).

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

'''

from random import random
class Solution:
    def __init__(self, w):
        '''
            Generate the cumulative sums array which will be used generate the random target based on weight of elements.
        '''
        self.prefix_sums =[]
        self.sum = 0

        for weight in w:
            self.sum += weight
            self.prefix_sums.append(self.sum)
        self.total = self.sum

    def pickIndex(self):

        left, right = 0, len(self.prefix_sums) - 1
        # calculate the target by multiplying the total * random, so this will indicate where the target is closer to the element in the array
        target = self.total * random()

        while left < right:
            mid = left + (right - left)//2
            if target < self.prefix_sums[mid]:
                right = mid
            else:
                left = mid + 1
        return left

def main():
    #l1 = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    l2 = [1,8,9]
    solution = Solution(l2)
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())



main()



'''
    Time complexity: Log(N)
    Space complexity: O(N) for the init and O(1) for pickIndex.
'''