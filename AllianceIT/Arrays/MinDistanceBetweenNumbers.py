# def solve(nums, x_target, y_target):
#
#     # check if the numbers are contained in the array
#     if x_target not in set(nums):
#         return -1
#
#     if y_target not in set(nums):
#         return -1
#
#     if len(nums)<1:
#         return -1
#
#     left  = 0
#     right = 0
#
#     for i in range(len(nums)):
#         if nums[i] == x_target:
#             left = i
#
#     for i in range(len(nums)):
#         if nums[i]== y_target:
#             right= i
#
#     return right - left
#
# def main():
#     nums = [3, 5, 5, 2, 6, 3]
#     nums2 = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8,  3]
#              0  1  2  3  4  5  6  7  8  9  10 11
#     x = 3
#     y = 6
#     x2 = 5
#     y2 = 6
#     print(solve(nums2,x,y))
#
# main()

import sys

def minDist(arr, x, y):
    # previous index and min distance
    prev = -1
    n = len(arr)
    min_dist = sys.maxsize

    for curr in range(n):
        if (arr[curr] == x or arr[curr] == y):
            # we will check if p is not equal to -1 and
            # if the element at current index matches with
            # the element at index p , If yes then update
            # the minimum distance if needed
            if (prev != -1 and arr[curr] != arr[prev]):
                min_dist = min(min_dist, curr - prev)
                # update the previous index
            prev = curr

            # If distance is equal to int max
    if (min_dist == sys.maxsize):
        return -1
    return min_dist

def main():
    # Driver program to test above function */
    arr = [3, 5, 5, 2, 6, 3]
    #n = len(arr)
    x = 5
    y = 6
    print("Minimum distance between %d and %d is %d\n" % (x, y, minDist(arr, x, y)));

main()