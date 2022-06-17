class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror_tree(root):
    # pre-order traversal
    if root == None:
        return 

    
    if root.left is not None:
        mirror_tree(root.left)

    if root.right is not None:
        mirror_tree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp



