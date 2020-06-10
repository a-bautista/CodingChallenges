"""Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
"""

def binary_search(arr, key):
    start, end = 0, len(arr)-1
    isAscending = arr[start] < arr[end]

    while start <= end:
        # calculate the middle of the current range
        # avoid overflow in Python
        mid = start + (end - start)//2

        if key == arr[mid]: # if the key found is found
            return mid

        if isAscending: # ascending order
            if key < arr[mid]: # the key can be in the first half
                end = mid - 1
            else:              # the key can be in the second half
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid -1
            else:
                start = mid + 1
    return -1 # element not found


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()