"""

    Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is
    the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

           1
         / \
        2   3
       / \
      4   5

    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

    We can use DFS to go down into each node and then we determine the max value between the answer and the sum of L+R+1 (+1
    in case you have reached lowest node).

"""

class Solution(object):

    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1