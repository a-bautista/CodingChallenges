'''
    Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
    The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in
    the subtree with root A.



Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation:
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".

Example 2:

Input: root = [1,2,3,4]
Output: [4]

Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]



'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left  = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.helper(root)
        return res[0]

    def helper(self,root):
        if root is None:
            return [None,0]

        left = self.helper(root.left)
        right = self.helper(root.right)

        maxh = max(left[1],right[1])
        if left[1] < right[1]:
            return [right[0],maxh+1]
        elif left[1] > right[1]:
            return [left[0],maxh+1]
        else:
            return [root,maxh+1]



def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.left.left.left = TreeNode(6)
    tree.left.left.right = TreeNode(7)

    solution = Solution()
    res = solution.lcaDeepestLeaves(tree)

    # print parent node
    print(res.val)

    # print children node
    print(res.left.val)
    print(res.right.val)

main()

"""
    Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might 
    be visiting all the nodes of the binary tree.

    Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack 
    would be NNN since the height of a skewed binary tree could be N. 

"""