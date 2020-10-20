'''
    Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any
    contiguous subarray of size ‘k’.
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

    k=3
    [2, 1, 5, 1, 3, 2]
     ^
     ^
     i
    sum = 2

    [2, 1, 5, 1, 3, 2]
     ^
        ^
        i
     sum = 3

    [2, 1, 5, 1, 3, 2]
     ^
           ^
           i
    sum = 8

    [2, 1, 5, 1, 3, 2]
        ^
              ^
              i

    sum = 7

    [2, 1, 5, 1, 3, 2]
           ^
                 ^
                 i

    sum = 9

    [2, 1, 5, 1, 3, 2]
              ^
                    ^
                    i

    sum = 6

    nums = [2, 1, 5, 1, 3, 2]
    start_window = 0
    end_window = 0
    max_val = float('-inf')
    for i in range(len(nums)):

        end_window+=1
        if (end_window-start_window)>=k-1:

            start_window +=1

        suma = nums[start_window]+nums[end_window]
        max_val = max(max_val, suma)

'''

def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  start_window = 0

  for end_window in range(len(arr)):
    window_sum += arr[end_window]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if end_window >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start_window]  # subtract the element going out
      start_window += 1  # slide the window ahead
  return max_sum


  # start_window = 0
  # end_window = 0
  # max_val = float('-inf')
  #
  # for _ in range(len(arr)):
  #     end_window += 1
  #     if (end_window - start_window) >= k :
  #         start_window += 1
  #     suma = arr[start_window] + arr[end_window]
  #     max_val = max(max_val, suma)
  # return max_val


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()