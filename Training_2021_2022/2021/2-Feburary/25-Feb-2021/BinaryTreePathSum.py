'''
Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

       1
     /  \
    2    3
  / \   / \
 4   5  6 7

 S =10
 Res = 1,3,6
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def solve(root, target):
    if root is None:
        return False

    # return True to indicate that there's a path that contains the target sum of nodes
    if root.val == target and root.left is None and root.right is None:
        return True

    # recursively get the values from the left and discount the target minus the root value
    # recursively get the values from the right and discount the target minus the root value
    return solve(root.left, target - root.val) or solve(root.right, target - root.val)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    res = solve(root, 28)
    print(res)

main()