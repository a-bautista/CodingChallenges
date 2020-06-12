
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

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []
        heapq.heapify(free_rooms)

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)