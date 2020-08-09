'''
    Given an unsorted list of start and end time, find **any** number within all the ranges that occurs in maximum number of intervals.
    input: [[1,4],[3,5],[4,6]]
    output: 4
    This is for non negative numbers.
    https://www.geeksforgeeks.org/maximum-occurred-integer-n-ranges/


'''

from collections import defaultdict

def get_max(intervals):
    start, end = defaultdict(int), defaultdict(int)
    # assumes non negative interval values
    min_start, max_end = float("inf"), 0

    # initialize the count of initial numbers and set the boundaries of the ending numbers
    for s, e in intervals:
        start[s] += 1
        end[e + 1] -= 1
        min_start = min(min_start, s)

        max_end = max(max_end, e + 1)

    active_intervals, max_count, res = 0, 0, 0
    for time in range(min_start, max_end):
        if time in start:
            # we increment the start time which means a new interval starts
            active_intervals += start[time]
        if time in end:
            # we decrement for each end time which means its the end of a past interval
            active_intervals += end[time]

        # We check  the number that is present among the running intervals
        if active_intervals > max_count:
            res = time
            max_count = active_intervals
    return res

def main():
    T = [([(1,15), (4,8), (3,5), (1,4)], 4),
        ([(1, 15), (5, 8), (9, 12), (13, 20), (21, 30)],5)]

    res = get_max([[1,15], [4,8], [3,5], [1,4]])
    print(res)
    for t in T:
        assert get_max(t[0]) == t[1]

main()

'''
    Time complexity: O(N+duration)
    duration = max_end - min_start
    Space: O(n)
'''