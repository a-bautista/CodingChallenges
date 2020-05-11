

from collections import deque
from typing import List


''''
    Requirements:
    
        Given the following list with elements, merge them so you can have 1 big list with all the elements. 
        [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6, 8, 10, 15, 18]]
        
        

'''


def main():
    solution = Solution.mergeIntervals(Solution, [[1, 3], [2, 6], [8, 10], [15, 18]])
    solution2 = Solution.mergeIntervals(Solution, [[1, 9], [2, 5], [19, 20], [10, 11], [12, 20], [0, 3], [0, 1], [0, 2]])
    print(solution)
    print(solution2)

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        q = deque()

        '''
        q.append(intervals[1])
        print(q[0][-1])
        print(q)
        if q[0][-1] >= q[1][0] and q[0][-1] <= q[1][1] :
            print(True)
            q.append(q[0]+[q[1][1]])
            q.popleft()
            q.popleft()

            #q[0] += q[1][1]
        print(q)
        '''

        q.append(intervals[0])
        for interval in intervals[1:]: # start from position 1 to the rest of the array
            q.append(interval)

            if q[0][-1] >= q[1][0] and q[0][-1] <= q[1][1] : # merge the first list elements of q with the last list element of the q
                q.append(q[0]+[q[1][1]]) # I am using a list inside of the q[1][1], so I can join the list element into the previous list
                q.popleft()  # remove interval k-2 where k is the total list of elements in the q
                q.popleft()  # remove interval k-1

            elif q[0][-1] <= q[1][0] and q[0][-1] <= q[1][-1]: # if the elements of the first list are all greater than the elements of all the elements of the second list
                q.append(q[0]+[q[1][0]]+[q[1][-1]]) # join the elements of the second list
                q.popleft()    # remove interval
                q.popleft()



        return [q]







if __name__ == '__main__' :
    main()