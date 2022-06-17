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
    3. If either the left or the right branch returns True then it means one of the two nodes was found.
    4. If at any point in the traversal, any two of the three flags left, right or mid becomes True, this means
        we have found the lowest common ancestor for the nodes p and q.

    Time Complexity: O(N), where N is the number of nodes in the binary tree.
    In the worst case we might be visiting all the nodes of the binary tree.

    Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be
    NNN since the height of a skewed binary tree could be N.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve_lca(root, p, q):
    lca = None
    def recurse_tree(root, p, q):
        nonlocal lca

        if not root:
            return False
        leftPath = recurse_tree(root.left, p, q)

        rightPath = recurse_tree(root.right, p, q)

        mid = root.val == p or root.val == q

        if mid + leftPath + rightPath >= 2:
            lca = root.val

        return mid or leftPath or rightPath

    recurse_tree(root, p, q)
    return lca


def main():
    #root = [3,5,1,6,2,0,8,None,None,7,4] 
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    p = 10 
    q = 12
    res = solve_lca(root, p, q)
    print(res)

main()


'''
        1
      /  \
     4   10
        /  \
       2    12

    1->4
    1->10->2
    1->10->12

'''