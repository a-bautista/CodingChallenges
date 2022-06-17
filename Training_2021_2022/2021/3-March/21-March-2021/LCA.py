class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lca = None

    def solve(self, root, p, q):

        self.recursive(root, p, q)
        return self.lca
        
    def recursive(self, root, p, q):

        if root is None:
            return False
        
        left = self.recursive(root.left, p, q)
        right = self.recursive(root.right, p, q)

        # mid can be either True or False which depends if root == p or root == q
        mid = root.val == p.val or root.val == q.val
        # if root.val == p.val or root.val == q.val:
        #     mid = root.val

        if mid + left + right >= 2:
            self.lca = root.val
        return mid or left or right
        

def main():
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    # root.left.left.left = TreeNode(3)
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    solution_lca = Solution()
    lca = solution_lca.solve(tree, TreeNode(6), TreeNode(5))
    print(lca)
    
main()