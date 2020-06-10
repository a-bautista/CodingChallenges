"""

    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

    Note:

        Given target value is a floating point.
        You are guaranteed to have only one unique value in the BST that is closest to the target.

    Example:

    Input: root = [4,2,5,1,3], target = 3.714286

        4
       / \
      2   5
     / \
    1   3

    Output: 4

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def closestValue(self, root, target):
        node = root.val
        while root:
            if abs(root.val - target) < abs(node - target):
                node = root.val
            root = root.left if target < root.val else root.right
        return node


def main():
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    solution = Solution()
    res = solution.closestValue(tree, 10.4)
    print(res)

main()

"""
    Time complexity : O(k) in the average case and O(H+k) in the worst case, 
    where k is an index of closest element. It's known that average case is a balanced tree, in that case stack always 
    contains a few elements, and hence one does 2k2k2k operations to go to kth element in inorder traversal 
    (k times to push into stack and then k times to pop out of stack). 
    That results in O(k)\mathcal{O}(k)O(k) time complexity
    Space complexity: O(K) because we depend on the number of leaves. 
"""