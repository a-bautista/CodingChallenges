'''
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element. 

    Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Heap solution: O(n*log(k))
    The optimal solution is the quick select.

'''

from heapq import *
def solve(nums, k):
    maxRes  = []
    #heapify(maxRes)
    for i in range(len(nums)):
        heappush(maxRes, nums[i])
        if k < len(maxRes):
            heappop(maxRes)
    # edge case
    if k>len(maxRes):
        return -1
    return maxRes[0]

def main():
    nums = [3,2,1,5,6,4]
    k = 2
    res = solve(nums, k)
    print(res)

main()

    

