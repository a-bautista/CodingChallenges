from collections import deque

def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutationsq = deque()
  permutationsq.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutationsq)
    for _ in range(n):
      existingPermutation = permutationsq.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(existingPermutation)+1):
        newPermutation = list(existingPermutation)
        newPermutation.insert(j, currentNumber)
        # start adding the results once your new permutation are of the same size as the length of the array
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        # keep adding the new permutations to the queue
        else:
          permutationsq.append(newPermutation)
  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

'''
    Time complexity: O(N*N!) because we know that N! is the time for getting all the permutation of a set with N numbers.
    Space complexity: O(N*N!)

'''