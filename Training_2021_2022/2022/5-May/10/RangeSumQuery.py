'''
    Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right 
    inclusive where left <= right.
    
    Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between
    indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

    Solution 1: Brute Force
    class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        curr_sum = 0
        for num in self.nums[left:right+1]:
            curr_sum += num

        return curr_sum

    Time complexity: O(N)
    Space complexity: O(1)

    Solution 2: Prefix sum

    You are going to create an array of all the computed values, for instance,
    given [-2, 0, 3, -5, 2, -1]  you will generate an array of precomputed values as
    
    [-2, -2, 1, -4, -2, -3]
      0   1  2   3   4   5

    Then if i and j are > 0 then return the subtraction between j and i-1 (inclusive)
    else just return the last value from the precomputed array.

    Time complexity: O(1) for giving the answers, O(N) for pre-computing values
    Space complexity: O(N)

'''


from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)

    def sumRange(self, i: int, j: int) -> int:
        # return self.sum[j] - self.sum[i - 1]
        if i > 0 and j > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            # print(self.sum[j])
            return self.sum[j]

def main():

    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    # numArray.nums = [-2, 0, 3, -5, 2, -1]
    # print(numArray.nums)
    print(numArray.sum)
    sol = numArray.sumRange(0,2)
    # sol2 = numArray.sumRange(2,5)
    # sol3 = numArray.sumRange(0,5)
    print(sol)
    # print(sol2)
    # print(sol3)

main()