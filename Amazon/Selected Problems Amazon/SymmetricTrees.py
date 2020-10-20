'''
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

          1
         / \
        2   2
      / \  / \
     3  4 4  3


        1
       / \
      2   2
      \   \
      3    3

     [1,2,2,null,3,null,3]


     Let's define symmetric, that is, symmetric in its shape and not in the values.
     If can traverse the Tree and I don't find any null values then I can say the tree is symmetrical
     Pre-order traversal
     We can use a Queue with a BFS approach, that will have a O(1) for insertions and deletions in the Queue and O(V+E) when
     doing the BFS.
'''

from collections import deque

def main():
    tree = TreeNode(1)
    tree.insert(tree, TreeNode(2))
    tree.insert(tree, TreeNode(2))
    tree.print_preorder(tree)

    solution = Solution.isSymmetric(Solution,tree)
    print(solution)

class TreeNode:
    def __init__(self,key):
        self.right = None
        self.left  = None
        self.val   = key

    def insert(self, root, node):

        '''Insert a node given the root value in the BST.'''
        # if root is None: # only if you declare tree = Node(None), not correct
        #    root = node
        #    print('base case')

        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)

    def print_preorder(self, root):

        if root:
            print(root.val)
            self.print_preorder(root.left)
            self.print_preorder(root.right)

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        q = deque([root.left, root.right])

        # BFS
        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2: # if not empty on either side
                continue

            # if there's a leaf node as None
            elif (not t1 or not t2) \
                    or \
                    (t1.val != t2.val): # if the left side is not the same as the right side
                return False

            q += [t1.left, t2.right, t1.right, t2.left]

        return True

if __name__ == '__main__':
    main()