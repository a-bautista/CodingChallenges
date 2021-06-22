'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:

Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

'''

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        sum = 0
        def visit(nestedList, depth=1):
            nonlocal sum
            for item in nestedList:
                if item.isInteger():
                    sum += item.getInteger()*depth
                else:
                    visit(item.getList(), depth+1)
        visit(nestedList)
        return sum

    '''
        input = [1,[4,[6]]]
                 ^
        first iteration, 1 is an integer and depth is 1, so 1*1 = 1
        input = [1,[4,[6]]]
                    ^
        second iteration, we have a list, so it's not an integer then go back again to the function 
        sum = 1 
        depth = 2
        
        so 2*4 = 8 and add this 8 to the previous sum which was 9
        third iteration, we have another list, so it's not an integer then go back to the function
        sum = 9
        depth = 3
        
        so 3*6 = 18 and 18 + 9 = 27 
    '''


def main():
    solution = Solution()
    l1 = [[1,1],2,[1,1]]
    res = solution.depthSum(l1)
    print(res)

main()


'''
    Time complexity: O(N)
    Space complexity: O(D) where D is the depth of the nested list.
'''