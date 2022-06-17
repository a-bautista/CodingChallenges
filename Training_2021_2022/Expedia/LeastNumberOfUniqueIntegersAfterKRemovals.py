'''
    Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
    Example 1:

    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.
    Example 2:
    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Get the count of our elements.
        cnts = collections.Counter(arr)
		# Create a heap with our counts.
        heap = [(v, k) for k, v in cnts.items()]
        heapq.heapify(heap)
		# Remove k from the cnts of the elements in our heap, always popping the lowest cnts.
        for _ in range(k):
            cnt, val = heapq.heappop(heap)
            cnt -= 1
            if cnt != 0:
                heapq.heappush(heap, (cnt, val))
        # The len of whats left in the heap is our answer.
        return len(heap)