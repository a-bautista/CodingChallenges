from collections import deque
def find_max_sliding_window(arr, window_size):
  result = []

  if len(arr) == 0:
    return result
  
  if window_size > len(arr):
    return result

  window = deque()
  
  #find out max for first window
  for i in range(0, window_size):
    # get the greatest element inside this window array
    while window and arr[i] >= arr[window[-1]]:
      window.pop()
    window.append(i)
  
  # insert the greatest element in the result list
  result.append(arr[window[0]])
  
  # start from where you left in the window 
  for i in range(window_size, len(arr)):
    #remove all numbers that are smaller than current number
    #from the tail of list, so the biggest element remains at the queue
    while window and arr[i] >= arr[window[-1]]:
      window.pop()

    #remove first number if it doesn't fall in the window anymore
    if window and (window[0] <= i - window_size):
      window.popleft()

    window.append(i)
    result.append(arr[window[0]])
  
  return result
    
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# print ("Array = " + str(array))
# print ("Max = " + str(find_max_sliding_window(array, 3)))
array = [7,2,4]
#array = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]  
print ("Array = " + str(array))
print ("Max = " + str(find_max_sliding_window(array, 2)))

'''

	from collections import deque
	def solve(nums, k):
		
		
			# 1. Get the current max window from 0 to k.
			# 2. Append the result of the max value from the window 0, to k in a list.
			# 3. Get the next max value in window k to len(nums)
			# 4. if the current value is greater than the last element in the window then do a pop
			# 	because we are interested in the greatest value
			# 5. do a pop to elements that do not fit in our window
			# 6. Append the results to the current list results			
		
		res = []
		queueWindow = deque()
		for i in range(0, k):
			while queueWindow and nums[i]>=queueWindow[-1]:
				queueWindow.pop()
			queueWindow.append(i)
			
		res.append(nums[queueWindow[0]])
		
		for i in range(k, len(nums)):
			# get the max element at the current window
			while queueWindow and nums[i]>=queueWindow[-1]:
				queueWindow.pop()
			
			# shrink the window if values are outside of the queueWindow
			if queueWindow and queueWindow[0]<= i - k:
				queueWindow.popleft()
				
			# get the next element in the window
			queueWindow.append(i)
			# this will be the greatest element to add
			res.append(nums[queueWindow[0]])

'''