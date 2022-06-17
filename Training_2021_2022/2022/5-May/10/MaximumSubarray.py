'''
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum 
    and return its sum.

    A subarray is a contiguous part of an array.

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    
    Output: 6
    
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Input: nums = [5,4,-1,7,8]
    
    Output: 23

    Solution: 

    Kadane's algorithm
    
    Whenever you see a question that asks for the maximum or minimum of something, 
    consider Dynamic Programming as a possibility. The difficult part of this problem 
    is figuring out when a negative number is "worth" keeping in a subarray.

'''

def solve(nums):

    max_sum = curr_sum = nums[0]

    # start with the second number because you already have the first one
    for num in nums[1:]:
        # get the sum of the current element + the next element in the array
        curr_sum = max(num, curr_sum + num)

        # maxSubArray is the final return value. Update it continuously whenever you
        # find a bigger subarray
        max_sum = max(max_sum, curr_sum)

    return max_sum

def main():

    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [1]
    res = solve(nums1)
    print(res)

main()