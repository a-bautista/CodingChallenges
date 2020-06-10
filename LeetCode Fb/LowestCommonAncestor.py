
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.lca = None


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        # Traverse the tree
        self.recurse_tree(root, p, q)
        return self.ans

    def recurse_tree(self, current_node, p, q):

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = self.recurse_tree(current_node.left, p, q)

        # Right Recursion
        right = self.recurse_tree(current_node.right, p, q)

        # If the current node is one of p or q
        mid = current_node.val == p.val or current_node.val == q.val

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            self.ans = current_node.val

        # Return True if either of the three bool values is True.
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
    lca = solution_lca.lowestCommonAncestor(tree, TreeNode(4), TreeNode(5))

    #result = tree.lowestCommonAncestor(tree,TreeNode(4), TreeNode(5))
    print("The LCA is : " + str(lca))



main()

"""
   Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
   The lowest common ancestor is defined between two nodes p and q as the lowest node in T that 
   has both p and q as descendants (where we allow a node to be a descendant of itself).
   
   Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
   Output: 3
   Explanation: The LCA of nodes 5 and 1 is 3.

   Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
   Output: 5
   Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
    
    Algorithm:
    
    1. Start traversing the tree from the root node.
    2. If the current node is either p or q, then mark the variable mid as True and continue to 
        search for the other node in the left and right branches. 
    3. If either of the left or the right branch returns True then it means one of the two nodes was found.
    4. If at any point in the traversal, any two of the three flags left, right or mid becomes True, this means
        we have found the lowest common ancestor for the nodes p and q. 
        

    Time Complexity: O(N)O(N)O(N), where NNN is the number of nodes in the binary tree. 
    In the worst case we might be visiting all the nodes of the binary tree.

    Space Complexity: O(N)O(N)O(N). This is because the maximum amount of space utilized by the recursion stack would be NNN since the height of a skewed binary tree could be NNN. 

"""

# class TreeNode:
#
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
#         self.lca = None
#
#
# class Solution:
#
#     def __init__(self):
#         # Variable to store LCA node.
#         self.ans = None
#
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         def recurse_tree(current_node):
#
#             # If reached the end of a branch, return False.
#             if not current_node:
#                 return False
#
#             # Left Recursion
#             left = recurse_tree(current_node.left)
#
#             # Right Recursion
#             right = recurse_tree(current_node.right)
#
#             # If the current node is one of p or q
#             mid = current_node.val == p.val or current_node.val == q.val
#
#             # If any two of the three flags left, right or mid become True.
#             if mid + left + right >= 2:
#                 self.ans = current_node.val
#
#             # Return True if either of the three bool values is True.
#             return mid or left or right
#
#         # Traverse the tree
#         recurse_tree(root)
#         return self.ans