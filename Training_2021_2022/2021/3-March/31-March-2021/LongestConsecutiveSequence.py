'''
    Given an unsorted array of integers, find the length of the longest
    consecutive elements sequence.

    Your algorithm should run in O(n) complexity.

    Example:

    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is
    [1, 2, 3, 4]. Therefore its length is 4.

    Solution:
        I need to iterate over a set and verify if the current_val + 1 is present against every element in the array.
        if it is present then do a count+=1, to keep track the longest valid sequence.
        Once you are out of the loop, do a max to compare the count vs the max_count, and store this value.
        Return the max_count.
'''

def solve(nums):
    setNums = set(nums)
    #count = 0
    maxCount = float('-inf')
    for current in setNums:
        count = 1
        while current + 1 in setNums:
            count+=1
            current+=1 # update the value
            maxCount = max(maxCount, count)
    return maxCount


    #     if i+1 in setNums:
    #         count+=1
    #         maxCount = max(maxCount, count)
    # return maxCount

def main():

    nums = [100, 4, 200, 1, 3, 2]
    res = solve(nums)
    print(res)

main()

