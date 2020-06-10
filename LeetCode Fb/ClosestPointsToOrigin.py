import heapq
from math import sqrt

'''
        minHeap: (distance1, p1), (distance2, p2), (distance3, p3), ...(dn, pn)
        Go through the minheap and pop K times --> result is the answer
        minHeap: (2, p1), (3, p2), (1,p3), (5,p4)
        k=2
        (1,p3), (2,p1)
        
        Keep the elements in a min heap
    '''

'''
# elegant solution
class Solution:
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points,
                               lambda p: p[0] * p[0] + p[1] * p[1])
'''

class Solution:
    def kClosest(self, points, k):
        associate = dict()
        for p in points: # O(n)
            associate[sqrt(p[0]**2 + p[1]**2)] = p # O(1)
        sorted = heapq.nsmallest(k, associate.values()) # O(n log k)
        return sorted


def main():
    nums = [[1,3],[-2,2]]
    solution = Solution()
    res = solution.kClosest(nums, 1)
    print(res)

main()
    # Time: O(nlogK), space: O(n).

        # Accepted solution from LeetCode
    #    for p in points:
        # the lowest elements will be at the top
    #        return heapq.nsmallest(K, points, key=lambda p: sqrt(p[0]**2+p[1]**2))



