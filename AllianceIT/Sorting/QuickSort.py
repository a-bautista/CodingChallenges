def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr
        # return helper_quicksort(nums, 0, len(nums)-1)

# def helper_quicksort(nums, begin, end):
#
#     if begin < end:
#         splitpoint = partition(nums, begin, end)
#
#         helper_quicksort(nums, begin, splitpoint-1)
#         helper_quicksort(nums, splitpoint+1, end)
#     return nums
#
#
# def partition(nums, begin, end):
#
#     pivot = nums[begin]
#     leftmark = begin+1
#     rightmark = end
#
#     done = False
#
#     while not done:
#         while leftmark<= rightmark and nums[leftmark] <= pivot:
#             leftmark +=1
#         while rightmark>= leftmark and nums[rightmark] >= pivot:
#             rightmark -=1
#
#         if rightmark < leftmark:
#             done = True
#         else:
#             nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]
#
#     nums[begin], nums[rightmark] = nums[rightmark], nums[begin]
#     return rightmark

def main():
    # for i in range(10):
    #     nums = [randrange(0, 1000) for _ in range(10)]
    #     print(quickSort(nums, 0, len(nums)-1))
    nums = [34,1,87,4,9]
    print(quickSort(nums, 0, len(nums) - 1))

main()