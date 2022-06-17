'''
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Example 1:

    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
    Example 2:

    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.
    Example 3:

    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0

    Algorithm

    Let
    Left hand side be empty, and
    Right hand side holds all weights.

    Step_#2:

    Iterate weight_i from 0 to (n-1)

    During each iteration, take away weight_#i from right hand side, check whether balance is met or not.

    If yes, then the index i is the pivot index.

    If no, put weight_#i on the left hand side, and repeat the process until balance is met or all weights are exchanged.

    Step_#3:

    Finally, if all weights are exchanged and no balance is met, then pivot index does not exist, return -1.

'''

def pivotIndex(nums):

    total_weight_left, total_weight_right = 0, sum(nums)

    for index, c_weight in enumerate(nums):
        total_weight_right -= c_weight

        if total_weight_left == total_weight_right:
            return index

        
        total_weight_left += c_weight
    
    return -1

def main():

    nums = [1,7,3,6,5,6]
    res = pivotIndex(nums)
    print(res)

main()