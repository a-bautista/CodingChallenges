'''
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node 
    values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's 
    descendants. The tree s could also be considered as a subtree of itself.

    Example 1:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2

    Given tree t:

      4 
     / \
    1   2

    Return true, because t has the same structure and node values with a subtree of s.

    Example 2:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0

    Given tree t:

      4
     / \
    1   2

    Return false. 

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isMatch(self, s, t):
        # base case when s and t are empty
        if not(s and t):
            return s is t 
        # base case when the root, the left and right children are the same
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): 
            return True
        if not s: 
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    #return isSubtree(s, t)

def main():
    tree1 = Node(3)
    tree1.left = Node(4)
    tree1.right = Node(5)
    tree1.left.left = Node(1)
    tree1.left.right = Node(2)
    #tree1.left.right.left = Node(9)
    
    tree2 = Node(4)
    tree2.left = Node(1)
    tree2.right = Node(2)

    solution = Solution()
    res = solution.isSubtree(tree1, tree2)
    print(res)

main()

'''
    Naive approach, O(|s| * |t|)
    For each node of s, let's check if it's subtree equals t. We can do that in a straightforward 
    way by an isMatch function: check if s and t match at the values of their roots, plus their subtrees 
    match. Then, in our main function, we want to check if s and t match, or if t is a subtree of a child of s.
'''