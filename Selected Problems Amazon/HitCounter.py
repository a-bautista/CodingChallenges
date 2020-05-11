from collections import deque
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.counter.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.counter and timestamp -self.counter[0] >= 300:
            self.counter.popleft()
        return len(self.counter)