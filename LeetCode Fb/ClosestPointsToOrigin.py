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


class Solution2:
    def kClosest(self, points, K):
        self.sort(points, 0, len(points) - 1, K)
        return points[:K]

    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p + 1, r, K)
            else:
                self.sort(points, l, p - 1, K)

    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a

'''
    Worst case the solution from above is O(N**2) with quicksort
    But In average, we can reach in logN times and don't need to sort all elements at every step.
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



