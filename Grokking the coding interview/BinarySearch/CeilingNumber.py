"""
    Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

    Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

    Example 1:

        Input: [1, 3, 8, 10, 15], key = 12
        Output: 4
        Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

"""

def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if key > arr[n-1]: # in case the key is bigger than the biggest number in the array
        return -1

    start, end = 0, n-1
    # the loop is broken by forcing either the start or end to become less or greater
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))

main()