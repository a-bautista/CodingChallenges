'''
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    

    Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

 '''

from heapq import *
def solve(nums, k):
    res = []
    for i in range(len(nums)):
        heappush(res, nums[i])
        # when the heap gets more elements greater than k then we will now that the first element in the heap
        # will be the kth largest element from the array
        if k<len(res):
            heappop(res)
    # K > len(res) means that we will store the entire list of more elements
    if k> len(res):
        return -1
    return res[0]


def main():
    nums = [3,2,3,1,2,4,5,5,6] 
    k = 4
    res = solve(nums, k)
    print(res)

main()
