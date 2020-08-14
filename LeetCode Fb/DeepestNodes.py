'''
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

'''

'''
  Intuitively, we should be traversing from the children to the parent and calculate the
  height from bottom. 
  So the null nodes would have height 0. The leaf nodes would have the
  height 1 and the root would have the max height.
 
  At each node, we keep a pair<height_of_node_from_bottom, node>. 
  At a given node, if we realize that the leftHeight == rightHeight, it means we have found the deepest subtree
  rooted at node. 
  If leftHeight > rightHeight, it means the deepest subtree must be rooted at left child. 
  If rightHeight > leftHeight, it means the deepest subtree must be rooted at right child.
  
  when you go to node 5 you will find the following 
  l: (1, TreeNode{val: 6, left: None, right: None})
  r: (2, TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}})
  
  when you are at the end of program and node 3 then you will get
  
  l: (3, TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}})
  r: (2, TreeNode{val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}})
  
  
'''

class Solution:
    def subtreeWithAllDeepest(self, root):
        def deep(root):
            if not root:
                return 0, None

            l = deep(root.left)
            r = deep(root.right)

            # if left root is greater than right node then the deepest node is at the left
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            # if right root is greater than left node then the deepest node is at the right
            elif l[0] < r[0]:
                return r[0] + 1, r[1]
            # this means we have found the deepest nodes and its children
            else:
                return l[0] + 1, root

        return deep(root)[1]

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''