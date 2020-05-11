"""
    (1,10), (2, 7), (3, 19), (8, 12)
    1. Sort elements by the first element in the array.
    2. Store the last element in a min heap because in this way we will make sure to keep always the lowest value at the top.
    3. Compare k[0][-1] with k[1][0]: (1, 10), (2, 7)
        3.1. If k[0][-1] > k[1][0] is True, then add this value to the min heap because it means that there is no meeting
            room available (the second interval is contained in the first interval).
        3.2. If 3.1 is False, then you can replace the first element in the heap  with this new element because it means
            that the value is not contained.
    4. Return the len of the heap.



"""


import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: # empty list
            return 0

        intervals.sort(key = lambda x:x[0])
        free_rooms =[]
        heapq.heapify(free_rooms)

        heapq.heappush(free_rooms, intervals[0][-1])

        for meeting in intervals:

            if free_rooms[0] <= meeting[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, meeting[1])

        return len(free_rooms)

