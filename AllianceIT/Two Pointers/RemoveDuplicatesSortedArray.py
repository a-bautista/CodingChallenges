'''
  Given an array of sorted numbers, remove all duplicates from it. You should not use any
  extra space; after removing the duplicates in-place return the length of the subarray
  that has no duplicate in it.
'''

def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    # If the current value in the array is different from the previous one
    if arr[next_non_duplicate - 1] != arr[i]:
      # set the pointer to the current value that was different
      arr[next_non_duplicate] = arr[i]
      # increase the pointer of the next non duplicate value
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate

def remove_duplicates2(nums):
    if not nums:
        return []

    res = []
    # for i in nums:
    #   if i not in res:
    #     res.append(i)
    [res.append(x) for x in nums if x not in res]
    return res
    #return res

def main():
  l = [2, 3, 3, 3, 6, 9, 9]
  print(remove_duplicates2(l))
  print(remove_duplicates(l))
  print(set(l))
  #print(remove_duplicates2([2, 2, 2, 11]))


main()
