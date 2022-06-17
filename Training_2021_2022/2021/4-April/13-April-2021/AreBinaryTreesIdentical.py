'''
    Given the roots of two binary trees, determine if these trees are identical or not. 
    Identical trees have the same layout and data at each node. Consider the following 
    two identical binary trees that have the same layout and data.

        100            100
       /   \           /  \
      50    60        50   60
             \             /
             98           98

    Not identical.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # they are empty then true
        if p is None and q is None:
            return True
        
        # one is empty and the other is not
        # if not p or not q:
        #    return False
        
        # recursive call to check if they are the same
        if p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        return False