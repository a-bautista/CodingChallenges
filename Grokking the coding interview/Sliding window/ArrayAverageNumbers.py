'''Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

    Output: [2.2, 2.8, 2.4, 3.6, 2.8]

'''


def solve(k, nums):
  window_sum = 0.0
  start = 0
  sol = []
  for end in range(len(nums)):
    # keep adding elements
    window_sum += nums[end]

    if end >= k - 1:
      sol.append(window_sum / 5)
      window_sum -= nums[start]  # discard the element start
      start += 1

  return sol


def find_averages_of_subarrays(K, arr):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
      result.append(windowSum / K)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result


def main():
  result = solve(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  #result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()

