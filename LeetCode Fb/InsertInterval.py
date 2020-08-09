'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


'''

# same as merge intervals
# time complexity : O(N*Log(N))
def insert1(intervals, newInterval):
    intervals.append(newInterval)

    res = []
    for i in sorted(intervals, key=lambda x:x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res


class Solution:
    def insert(self, intervals, newInterval):

        # edge cases
        if not newInterval:
            return intervals
        if not intervals:
            return []

        # get the new values of the interval
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # In case the new interval's first value is greater than the first value of intervals
        #  then add the first values from intervals to the result because we will merge them due to overlap
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add the newInterval values to the result if there is no overlap
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap in output and intervals, merge the last value of output with the new interval last value
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add the next intervals to the results and verify if there's an overlap with the output results
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output

def main():
    intervals = [[1,3],[6,9]]
    interval = [2,5]
    #intervals = [[1,2],[8,9]]
    #interval = [0,3]
    solution = Solution()
    res = solution.insert(intervals,interval)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''
