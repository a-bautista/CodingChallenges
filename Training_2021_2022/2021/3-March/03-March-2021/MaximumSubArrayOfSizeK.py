'''
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous (sliding window)
    subarray of size ‘k’.

    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

    Negative numbers are not allowed in the array.
'''

def solve(nums, k):
    # edge cases: k<0 return -1
    # edge case: len(nums)==0 return -1
    if len(nums)==0 or k<=0:
        return -1

    # define the starting points of the sliding window and the count value
    start_window, max_sum = 0, 0
    cumulative = 0

    # set the for loop to iterate through the array
    for end_window in range(len(nums)):
        cumulative += nums[end_window]

        # determine if you have reached the threshold in k
        if end_window >= k-1:
            # determine if the current sum in cumulative has the maximum sum
            max_sum = max(max_sum, cumulative)
            # shrink the window from the initial position
            cumulative-= nums[start_window]
            # move the initial position to the next element
            start_window+=1
    return max_sum

def main():
    nums = [2, 1, 5, 1, 3, 2]
    k=3
    res = solve(nums, k)
    print(res)


main()

