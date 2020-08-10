class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # reduce k to go deep into level
            k -= 1
            # if k==0
            if not k:
                return root.val
            root = root.right

'''
Time complexity: O(H+k) where H is a tree height. This complexity is defined by the stack, 
which contains at least H+kH elements, since before starting to pop out one has to go down to a leaf. 
This results in O(log⁡N+k) for the balanced tree and O(N+k) for  completely unbalanced tree with all the 
nodes in the left subtree.

Space complexity: O(H) to keep the stack, where HHH is a tree height. 
That makes O(N)in the worst case of the skewed tree, and O(log⁡N) in the average case of the balanced tree. 
'''