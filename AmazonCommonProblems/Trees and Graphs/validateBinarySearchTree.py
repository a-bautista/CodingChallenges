'''
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



    Example 1:

        2
       / \
      1   3

    Input: [2,1,3]
    Output: true


      5
     / \
    1   4
       / \
      3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

    Req:

        I am printing in pre-order to get the values as described.
        I can do a comparison of each node in a pre-ordering approach to verify if the tree is correct or not, so I can have like a list
        of True values and if there's one value with False then the tree is not correct.
        Binary search? O(log(n)) as the average case



        def validate(tree, l):

            #results = []

            if tree:
                if tree.left or tree.right:
                    if tree.val < tree.left: # you cannot compare because there will be null values
                        l.append('True')
                    elif  tree.val > tree.right:
                        l.append('True')
                    else:
                        l.append('False')
                validate(tree.left)
                validate(tree.right)


'''

class Node():
    def __init__(self, key):
        self.right = None
        self.left  = None
        self.val   = key

def insert(tree, node):
    if tree.val < node.val:
        if tree.right is None:
            tree.right = node
        else:
            insert(tree.right, node) # go on to the next node to the right
    else:
        if tree.left is None:
            tree.left = node
        else:
            insert(tree.left, node)

def print_preorder(tree):

    if tree:
        print(tree.val)
        #print_preorder(tree.right)
        print_preorder(tree.left)
        print_preorder(tree.right)

def validate(tree,l):

    if tree:
        if tree.left or tree.right:
            if tree.val < tree.left:  # you cannot compare because there will be null values
                l.append('True')
            elif tree.val > tree.right:
                l.append('True')
            else:
                l.append('False')

        validate(tree.left,l)
        validate(tree.right,l)
