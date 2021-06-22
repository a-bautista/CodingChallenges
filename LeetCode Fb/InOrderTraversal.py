'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

'''
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

# recursively
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

'''
    Time complexity: O(N)
    Space complexity: O(N)
    This applies for both approaches.
'''

# iteratively
def inorderTraversal(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = inorderTraversal(root)
    print(res)

main()