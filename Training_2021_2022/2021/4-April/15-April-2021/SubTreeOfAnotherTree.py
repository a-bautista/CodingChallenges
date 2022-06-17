class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isMatch(self, root1, root2):

        # if you have reached to the bottom of the tree and you found Nones, then it means 
        # the structure is the same for the tree and subtree
        if not (root1 and root2):
            return root1 == root2

        if root1.val == root2.val and \
            self.isMatch(root1.left,root2.left) and \
            self.isMatch(root1.right,root2.right):
            return True

    def isSubTree(self, root1, root2):

        # check the first time if we have a match
        if self.isMatch(root1, root2):
            return True

        # there's not a tree
        if not root1:
            return False

        # if you have found that the subtree root2 is located in left of root1 and not right of root1 then
        # return True or if you have found that the subtree root2 is located in the right of root1
        # but not in the left of root1 then return True
        return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)

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
    res = solution.isSubTree(tree1, tree2)
    print(res)
    
main()