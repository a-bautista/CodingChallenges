def find_subsets(nums):
  total_subset = []
  # start by adding the empty subset
  total_subset.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(total_subset)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      temp_set = list(total_subset[i])
      temp_set.append(currentNumber)
      total_subset.append(temp_set)

  return total_subset


def main():

  #print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()


"""
    Time complexity #
    
    Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, the time complexity 
    of the above algorithm is O(2^N), where ‘N’ is the total number of elements in the input set. 
    This also means that, in the end, we will have a total of O(2^N) subsets.
    
    Space complexity #

    All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, 
    the space complexity of our algorithm is also O(2^N).
"""