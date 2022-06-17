'''
    Given an array of integers and a value K find a subsequence having maximum sum under K.
    Return the maximum Sum.

    // Examples - 

    nums = [1,2,3,4,5,6,7,16], K = 15
    // ans = 15
    // explaination = [1,2,3,4,5]

    nums = [1,2,3,12,3], K = 10
    // ans = 9
    // explaination = [1,2,3,3]
'''

def SubsequenceWithMaxSumUnderK (lst, k):
  collector_array = []
  for i in range(len(lst)):
    # sum resets after every loop
    sum = 0
    for j in range(i, len(lst)):
      # choose first element from list
      # if sum + lst[j] <= k, then keep adding the next element
      # Store sum in an collector Array
      # then filter out the possibility for a 
      # return the max element in the Array

      if (sum + lst[j]) <= k:
        sum += lst[j]
      
    collector_array.append(sum)

  final_array = list(filter(lambda x: x <= k, collector_array))

  return max(final_array)

def main():

    nums = [1,2,3,12,3]
    k = 10
    res = SubsequenceWithMaxSumUnderK(nums, k)
    print(res)

main()