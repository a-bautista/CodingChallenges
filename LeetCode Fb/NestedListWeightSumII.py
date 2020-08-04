'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.

Example 2:

Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.


'''

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum

'''
    Solution is BFS and single pass
    Time complexity: O(N)
    Space complexity: O(1)
'''