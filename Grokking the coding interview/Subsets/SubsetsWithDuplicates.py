def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  total_subset = []
  total_subset.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    currentNumber = nums[i]
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex + 1
    endIndex = len(total_subset) - 1
    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      temp_set = list(total_subset[j])
      temp_set.append(currentNumber)
      total_subset.append(temp_set)
  return total_subset


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()