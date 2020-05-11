'''
    Binary Search Tree, is a node-based binary tree data structure which has the following properties:
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.
'''

def main():
    #tree1 = Node(None) # fails when you declare a None value
    #insert(tree1, 1)


    tree = Node(8)
    insert(tree, Node(50))
    insert(tree, Node(-1))
    insert(tree, Node(55))
    insert(tree, Node(5))
    insert(tree, Node(4))
    '''
         8
       /   \
      -1    50
        \    \
        5     55
        /
       4 
    
    '''
    print('Calculate the O(n) for each value')
    print('In order traversal')
    print_in_order(tree)

    print('Pre order traversal')
    print_pre_order(tree)

    print('Post order traversal')
    print_post_order(tree)

    print('Range of numbers in a tree')
    calculate_nmb_range(tree,1,50)

    print('Delete node 4')
    deleteNode(tree, 4)

    print('In order traversal')
    print_in_order(tree)

    #print('Max Depth')

    print("Max depth: "+str(maxDepth(tree)))

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):

    '''Insert a node given the root value in the BST.'''
    #if root is None: # only if you declare tree = Node(None), not correct
    #    root = node
    #    print('base case')

    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def print_in_order(root):
    '''Print in-order the tree:
        8
      /  \
    -1   50

    result: -1, 8, 50.
    left, center, right
    useful for printing nodes from the lowest to the highest value

    '''
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)

def print_pre_order(root):
    '''Print pre-order the tree:

        8
      /  \
    -1   50

    result: 8, -1, 50
    center, left, right
    useful for copying a tree
    '''

    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)

def print_post_order(root):
    '''Print pre-order the tree:

        8
      /  \
    -1   50

    result: -1, 50, 8
    left, right, root
    useful for deleting a node
    '''
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)


def calculate_diameter(root):
    pass


def maxDepth(root):
    if root is None:
        return 0
    else:
        # compute the depth of each subtree
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)

        # use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1



# Function to return the maximum
# heights among the BSTs
def maxHeight(a: list, n: int) -> int:
    # Create a BST starting from
    # the first element
    rootA = Node(a[0])
    for i in range(1, n):
        rootA = insert(rootA, a[i])

        # Create another BST starting
    # from the last element
    rootB = Node(a[n - 1])
    for i in range(n - 2, -1, -1):
        rootB = insert(rootB, a[i])

        # Find the heights of both the trees
    A = maxDepth(rootA) - 1
    B = maxDepth(rootB) - 1

    return max(A, B)


def calculate_nmb_range(root, k1, k2):
    '''Print the values between a range of numbers.
    This will be achieved with a in order traversal tree.'''

    if root is None:
        return       # empty return

    if k1<root.val:
        calculate_nmb_range(root.left,k1, k2)

    if k1 <= root.val <= k2:
        print(root.val)

    if k2 > root.val:
        calculate_nmb_range(root.right, k1, k2)


# Given a non-empty binary search tree, return the node
# with minum key value found in that tree. Note that the
# entire tree does not need to be searched
def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

        # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

        # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif (key > root.val):
        root.right = deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

            # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.val = deleteNode(root.right, temp.val)
    return root


if __name__ == '__main__':
    main()