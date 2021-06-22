'''
    Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

    Input: nums = [[1,2,3],[4,5,6],[7,8,9]]

        [1,2,3]
        [4,5,6]
        [7,8,9]

    Elements are all up in the diagonal.
    Output: [1,4,2,7,5,3,8,6,9]
    Same analogy applies to all nodes nums[i][j]

'''

from collections import deque
class Solution:
    def findDiagonalOrder(self, nums):
        ans = []
        rows = len(nums)

        # We can think of the given matrix as a tree and use BFS to solve this problem.
        # The top-left number, nums[0][0], is the root node. nums[1][0] is its left child and nums[0][1] is its right child.
        # (0,0) pop
        # (1,0) pop, (0,1) right
        # (0,1) pop, (2,0) left, (1,1) right
        # (2,0) pop, (1,1) right, (0,2) left
        # (1,1) pop, (0,2), (2,1)

        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            # add the x,y coordinate of the matrix to the result
            ans.append(nums[row][col])
            # we only add the number at the bottom if we are at column 0 because that represents the
            # left child of the tree
            if col == 0 and row + 1 < rows:
                queue.append((row + 1, col))
            # add the number on the right or add the right child
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return ans

def main():
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    res = solution.findDiagonalOrder(nums)
    print(res)

main()