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

