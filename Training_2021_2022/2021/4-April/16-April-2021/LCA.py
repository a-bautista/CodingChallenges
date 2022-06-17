'''
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    The lowest common ancestor is defined between two nodes p and q as the lowest node in T that
    has both p and q as descendants (where we allow a node to be a descendant of itself).

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself 
    according to the LCA definition.


    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.lca = None

class Solution:
    def solve(self, root, p, q):
        self.lca = None
        self.solve_lca(root, p, q)
        return self.lca

    def solve_lca(self, root, p, q):

        if not root:
            return False
        
        left = self.solve_lca(root.left, p, q)
        right = self.solve_lca(root.right, p, q)

        mid = root.val == p.val or root.val == q.val

        if mid + left + right >=2:
            self.lca = root.val
        
        return mid or left or right

def main():
    # tree = TreeNode(1)
    # tree.left = TreeNode(2)
    # tree.right = TreeNode(3)
    # tree.left.left = TreeNode(4)
    # tree.left.right = TreeNode(5)
    # tree.right.left = TreeNode(6)
    # tree.right.right = TreeNode(7)
    # solution_lca = Solution()
    # lca = solution_lca.solve(tree, TreeNode(6), TreeNode(7))
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    p = Node(1)
    q = Node(8)
    solution = Solution()
    lca = solution.solve(root, p, q)
    #result = tree.lowestCommonAncestor(tree,TreeNode(4), TreeNode(5))
    print("The LCA is : " + str(lca))

main()
        