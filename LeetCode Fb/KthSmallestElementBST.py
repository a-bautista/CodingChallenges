'''
Given a binary search tree, write a function kthSmallest to find
 the kth smallest element in it.



Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

'''

class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        # do the in-order traversal (left, root, right)
        self.helper(node.left)
        self.k -= 1
        # when k==0 then it means I have found the node
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)

'''
Recursive solution (in-order BST traversal) complexity:

In worst case, we visit every node O(N) time.
We add to the call stack, our space complexity is O(d) 
- the max depth of recursion. 
For a balanced BST this is O(logN), but could be O(N) if 
the tree is unbalanced.
Space: o(1)?

'''