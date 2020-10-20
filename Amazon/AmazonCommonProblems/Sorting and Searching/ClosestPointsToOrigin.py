import heapq
import math

'''
        minHeap: (distance1, p1), (distance2, p2), (distance3, p3), ...(dn, pn)
        Go through the minheap and pop K times --> result is the answer
        minHeap: (2, p1), (3, p2), (1,p3), (5,p4)
        k=2
        (1,p3), (2,p1)
    '''

class Solution:
    def kClosest(self, List):
        pass

    '''
        #easy solution
        heap = heap[]
        heapq.heapify(heap)
        for p in points:
            # the lowest elements will be at the top
            heapq.heappush(heap, (math.sqrt(p[0]**2 + p[1]**2, p)))
        return [heapq.nsmallest(K, heap)]
        
        # Accepted solution from LeetCode
        for p in points:
        # the lowest elements will be at the top
            return heapq.nsmallest(K, points, key=lambda p: sqrt(p[0]**2+p[1]**2))
    '''