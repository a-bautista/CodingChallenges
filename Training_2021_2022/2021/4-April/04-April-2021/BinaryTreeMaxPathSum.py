'''
        Find the path with the maximum sum in a given binary tree.
        Write a function that returns the maximum sum.
        A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily
        pass through the root.


        Binary Tree Maximum Path Sum
        -10
        /   \
    9     20
            /  \
        15    7

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def solve(self, root):
        self.res = float('-inf')
        self.rec(root)
        return self.res

    def rec(self, root):
        
        if not root:
            return 0

        left = max(self.rec(root.left), 0)
        right = max(self.rec(root.right), 0)
        newPath = root.val + left + right
        self.res = max(self.res, newPath)
        return max(left, right)+root.val

def main():

    tree             = TreeNode(12)
    tree.left        = TreeNode(7)
    tree.right       = TreeNode(1)
    tree.left.left   = TreeNode(9)
    tree.right.left  = TreeNode(10)
    tree.right.right = TreeNode(5)

    solution = Solution()
    res = solution.solve(tree)
    print(res)

main()

