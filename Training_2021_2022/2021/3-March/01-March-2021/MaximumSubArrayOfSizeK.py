'''
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of
    size ‘k’.

    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

'''

def max_sub_array_of_size_k(k, nums):
    sum_window, max_sum = 0,0
    start_window = 0
    for end_window in range(len(nums)):
        sum_window += nums[end_window]
        if end_window >= k-1:
            max_sum = max(sum_window, max_sum)
            sum_window -= nums[start_window]
            start_window +=1
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

'''
    time complexity: O(N)
    space complexity: O(1)
'''