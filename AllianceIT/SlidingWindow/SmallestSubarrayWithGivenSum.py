'''
    Given an array of positive numbers and a positive number ‘S’, find the length of the
    smallest contiguous subarray whose sum is greater than or equal to ‘S’.
    Return 0, if no such subarray exists.

    Example 1:

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
'''

def solve(nums, k):
    window_sum = 0
    start_window = 0
    min_length = float('inf')

    if k < 0:
        return 0

    for end_window in range(len(nums)):
        window_sum += nums[end_window]

        # shrink the window when the sum is equal or greater than the target
        while window_sum >= k:
            min_length = min(min_length, end_window - start_window + 1)
            window_sum -= nums[start_window]
            start_window +=1
    return min_length


def main():
    nums = [2, 1, 5, 2, 3, 2]
    k = 5
    print(solve(nums, k))

main()

'''
    Time complexity: O(N)+O(N) = 2*O(N) = O(N)
    Space complexity: O(1)
'''