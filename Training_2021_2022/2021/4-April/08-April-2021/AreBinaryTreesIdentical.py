'''
    Given the roots of two binary trees, determine if these trees are identical or not. 
    Identical trees have the same layout and data at each node. Consider the following 
    two identical binary trees that have the same layout and data.

        100            100
       /   \           /  \
      50    60        50   60
             \             /
             98           98

    Not identical.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def areTheSame(root1, root2):
    # default case
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        # check the center, the left and right of both trees recursively
        return (root1.val == root2.val and areTheSame(root1.left, root2.left) and areTheSame(root1.right, root2.right))
    
    return False

def main():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    res = areTheSame(root1, root2)
    print(res)

main()