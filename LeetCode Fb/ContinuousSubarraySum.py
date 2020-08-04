"""
    Given a list of non-negative numbers and a target integer k, write a function to check if the array has a
    continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n
     is also an integer.

     Input: [23, 2, 4, 6, 7],  k=6
     Output: True
     Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

     Input: [23, 2, 6, 4, 7],  k=42
     Output: True
     Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""

from collections import defaultdict
def checkSubarraySum(nums, k):
    cache = {}
    #cache2 = defaultdict(list)
    cur = 0
    for i, x in enumerate(nums):
        if cur not in cache:
            cache[cur] = i
            #cache2[cur].append(i)
        cur = (cur + x) % k if k != 0 else cur + x
        # if cur in cache means if cur is an index contained in cache
        if cur in cache and i > cache[cur]: return True
    return False

def main():

    nums = [23, 2, 6, 4, 7]
    k = 11
    res = checkSubarraySum(nums, k)
    print(res)

main()

"""
    Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
"""