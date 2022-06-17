'''
    In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
    Return the element repeated N times.

    Input: [1,2,3,3]
    Output: 3

    Example 2:
    # twist, give me the element with the most repeated values
    Input: [2,1,2,5,3,2,3]
    Output: 2
'''
from collections import Counter
def solve(nums):
    counter = Counter(nums)
    maxCount = float('-inf')
    for k in counter:
        maxCount = max(maxCount, counter[k])
    return maxCount

def main():
    nums = [2,1,2,5,3,2,3]
    res = solve(nums)
    print(res)

main()