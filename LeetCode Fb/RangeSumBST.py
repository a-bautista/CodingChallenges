
"""
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