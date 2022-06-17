'''
    Given a non-empty array of integers, return the k most frequent elements.

    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]
'''
from collections import Counter
from heapq import *
def solve(nums, k):
    # hash_map that contains the frequency of numbers
    counter = Counter(nums)
    minHeap = []

    # create a list with the lowest values at the beginning
    for number, total_count in counter.items():
        # the heap needs to contain the lowest element at the beginning, so we can heappop the first elements
        # we sort the heap by the total count of numbers, not by the index number
        heappush(minHeap, (total_count, number))
        if len(minHeap) >k:
            # the elements with the largest values are left in the heap
            heappop(minHeap)
    
    # convert the list of top k numbers
    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1])
    
    return topNumbers
    

def main():
    nums = [1,1,1,2,2,3,3,4] 
    nums2 = [-1,-1]
    k = 2
    res = solve(nums, k)
    print(res)

main()

    
'''
    The time complexity of the above algorithm is O(N+N∗logK)
    Space complexity: O(N)
'''
    








