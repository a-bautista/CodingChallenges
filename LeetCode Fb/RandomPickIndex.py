'''

Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

'''


from random import randint

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):

        res   = -1
        count = 0

        for i, x in enumerate(self.nums):
            if target == x:
                count += 1
                chance = randint(1, count)
                if count == chance:
                    # in case you are given an array with different numbers
                    # then just return the index of that character when it appeared
                    res = i
        return res

def main():
    l1 = [1,2,3,3,3]
    solution = Solution(l1)
    #solution.nums = l1
    res = solution.pick(2)
    print(res)

main()


'''
        Time complexity: O(n) where n is the size of the array of numbers
        Space complexity: O(k) where k is the number of times the target appeared
'''