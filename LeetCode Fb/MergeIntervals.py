from typing import List

def main():

    #solution = Solution.merge(Solution,[[1, 3], [2, 6], [8, 10], [7, 18]])
    #solution2 = Solution.merge(Solution, [[1,9], [2, 5], [19, 20], [10, 11], [12,20], [0,3], [0,1], [0,2]])
    #print(solution)
    #print(solution2)
    solution = Solution()
    res = solution.merge([[1,5], [3,7], [4,6], [6,8], [10,12], [11,15]])
    print(res)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by index 0
        intervals.sort(key=lambda x: x[0])
        #print(intervals)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.

            # not merged = not empty list
            # merged[-1][1] = get the last list and get the element in the position 1
            # if the last element of merged[-1][1] is less than the first element of the next list,
            # then elements do not overlap and you can add them to the list
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == '__main__':
    main()


    '''
        Given a collection of intervals, merge all overlapping intervals.

        Example 1:

        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
        
        Time complexity
        We use sorting in this case for doing the comparison of the intervals. 
        The time complexity is O(n log n) for all 
        sorting techniques in the worst case.
        
        Space complexity is O(1) or O(n).
        
    '''