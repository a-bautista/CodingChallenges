'''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

def solve(intervals):

    intervals.sort(key=lambda x:x[0])
    merged = []
    for interval in intervals:

        # not overlapping
        # the merged[-1][1] the last element is less than the current element in the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

def main():
    #solution = Solution()
    #res = solution.merge([[1,5], [3,7], [4,6], [6,8], [10,12], [11,15]])
    res =  solve([[1,5], [3,7], [4,6], [6,8], [10,12], [11,15]])
    print(res)

main()
