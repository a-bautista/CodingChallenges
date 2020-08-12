'''

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

'''

def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  # add the empty subset to the general subsets list
  subsets.append([])

  # these pointers will be used to avoid inserting the duplicate value into the results
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1

    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      set = list(subsets[j])
      set.append(nums[i])
      # append the subset to the general list
      subsets.append(set)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

main()

'''
  Time complexity: O(2**N) where N is the total number of elements in the input set.
  Space complexity: O(2**N)
'''