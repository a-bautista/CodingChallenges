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


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
