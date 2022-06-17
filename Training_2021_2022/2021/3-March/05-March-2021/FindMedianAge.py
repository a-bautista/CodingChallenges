from heapq import *
# class median_of_ages:

#   maxHeap = []
#   minHeap = []

#   def insert_age(self, num):
#     # if the maxHeap is empty or the first element is 
#     if not self.maxHeap or -self.maxHeap[0] >= num:
#       heappush(self.maxHeap, -num)
#     else:
#       heappush(self.minHeap, num)

#     if len(self.maxHeap) > len(self.minHeap) + 1:
#       heappush(self.minHeap, -heappop(self.maxHeap))
#     elif len(self.maxHeap) < len(self.minHeap):
#       heappush(self.maxHeap, -heappop(self.minHeap))

#   def find_median(self):
#     # we have even numbers
#     if len(self.minHeap)==len(self.maxHeap):
#         return -self.maxHeap[0] / 2 + self.minHeap[0] /2    
#     # we have 1 more element in the max heap than the min heap
#     return -self.maxHeap[0] / 1.0


class Solution:

    minHeap = []
    maxHeap = []
    def insert_age(self, single_num):
        # insert into heaps
        if (not self.maxHeap or -self.maxHeap[0]>=single_num):
            heappush(self.maxHeap, -single_num)
        else:
            heappush(self.minHeap, single_num)

        # do the swap of numbers
        # in case you have more elements in maxHeap than in minHeap, remove an element from minHeap and insert it into
        # the maxHeap
        if (len(self.maxHeap) > len(self.minHeap)+1):
            heappush(self.minHeap, -heappop(self.maxHeap))
        # in case you have more elements in minHeap than in maxHeap, remove an element from maxHeap and insert it into
        # the minHeap
        elif (len(self.maxHeap) < len(self.minHeap)):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        # if the 2 heaps have the same length
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2
        return -self.maxHeap[0] / 1.0

def main():
    solution = Solution()
    solution.insert_age(10)
    solution.insert_age(4)
    solution.insert_age(7)
    solution.insert_age(12)
    solution.insert_age(8)
    print(solution.find_median())

    #medianAge = median_of_ages()
    #medianAge.insert_age(22)
    #medianAge.insert_age(35)

    # medianAge.insert_age(10)
    # medianAge.insert_age(4)
    # medianAge.insert_age(7)
    # medianAge.insert_age(12)
    #medianAge.insert_age(5)
    #print(medianAge.find_median())

main()

'''
    Time complexity:
        insert age: O(Log(n))
        find_median: O(1)
    Space complexity:O(n)

'''