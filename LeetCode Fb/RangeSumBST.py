
"""
    Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

     10
   /    \
  5      15
 / \    /  \
3   7 None  18

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


    We traverse the tree using a depth first search. If node.val falls outside the range [L, R],
    (for example node.val < L), then we know that only the right branch could have nodes with value inside [L, R].
    DFS


"""

def rangeSumBST(self, root, L, R):
    def dfs(node):
        if node:
            if L <= node.val <= R:
                self.ans += node.val
            if L < node.val:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)

    self.ans = 0
    dfs(root)
    return self.ans