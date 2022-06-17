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
    hash_set = set(nums)
    max_value = float('-inf')

    for value in hash_set:
        curr_num = value
        count = 1
        while curr_num + 1 in hash_set:
            count+=1
            curr_num+=1
            max_value = max(max_value, count)
    return max_value

def main():
    nums = [100, 4, 200, 1, 3, 2]
    nums2 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    nums3 = [5,3,3,0,1,2,2]
    nums4 = [100, 1, 2, 3, 99]
    res = solve(nums)
    print(res)

main()