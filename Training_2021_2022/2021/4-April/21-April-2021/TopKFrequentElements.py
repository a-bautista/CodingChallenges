'''
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.
    
    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]
'''
from heapq import *
from collections import Counter
def solve(nums, k):
    counter = Counter(nums)
    freqNumbers = []
    res = []
    for number, freq in counter.items():
        heappush(res, (-freq, number))
    
    return [heappop(res)[1] for _ in range(k)]


def main():
    nums = [1,1,1,2,2,3] 
    k = 2
    res = solve(nums, k)
    print(res)

main()