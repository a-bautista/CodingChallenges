'''
    You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

    horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
    verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
    Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. 
    Since the answer can be a large number, return this modulo 10^9 + 7.

    Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
    Output: 4 
    
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. 
    After you cut the cake, the green piece of cake has the maximum area.

    Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
    Output: 6
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. 
    After you cut the cake, the green and yellow pieces of cake have the maximum area.

    TC: O(N*Log(N) + M*Log(N))
    SC: O(1)

'''
from typing import List

def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        maxHeight = maxWidth = 0
        for i, cut in enumerate(horizontalCuts):
            if i == 0:
                maxHeight = max(maxHeight, cut)
            else:
                maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i-1])
        
        # We also need to check the height from the last cut to the bottom of the cake!
        maxHeight = max(maxHeight, h - horizontalCuts[-1])  
                
        for i, cut in enumerate(verticalCuts):
            if i == 0:
                maxWidth = max(maxWidth, cut)
            else:
                maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i-1])
        
        # Also need to check the width from the last cut to the right of the cake!
        maxWidth = max(maxWidth, w - verticalCuts[-1])
        
        return maxHeight*maxWidth % MOD

def main():

    solution = maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1])
    print(solution)

main()
