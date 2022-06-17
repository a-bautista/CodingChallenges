'''
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

        1
      /  \
     2    3     
    / \
   4  5

    Output: 3 because [4,2,1,3] or [5,2,1,3] and you don't count the initial node

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        (res1, res2) = self.helper(root)
        # we return the number of nodes -1 which is equal to the number of edges
        # No. of nodes - 1 = edges
        return max(res1, res2) - 1

    def helper(self, root):
        if not root:
            return (0, 0)
        (left1, left2) = self.helper(root.left)
        (right1, right2) = self.helper(root.right)

        internalPath = max(left2, right2)
        if (left1 + right1 + 1) > internalPath:
            internalPath = left1 + right1 + 1

        return (max(left1, right1) + 1, internalPath)

        '''
            We have 3 cases:
                1. Case I: When the longest path is in the left side.
                2. Case II: When the longest path is in the right side.
                3. Case III: When the longest path is the left and right + the middle node (1 to denote it)
        '''
def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.right = Node(3)
    # root.left = Node(2)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.left.right = Node(7)
    # root.left.right.right = Node(7)
    # root.left.right.right.right = Node(8)
    # root.left.right.right.right.right = Node(9)
    # root.left.right.right.right.right.right = Node(10)

    # root.left.right.left = Node(6)
    # root.left.right.left.left = Node(11)
    # root.left.right.left.left.left = Node(12)
    # root.left.right.left.left.left.left = Node(13)
    # root.left.right.left.left.left.left.left = Node(14)




    solution = Solution()
    res = solution.diameterOfBinaryTree(root)
    print(res)

main()