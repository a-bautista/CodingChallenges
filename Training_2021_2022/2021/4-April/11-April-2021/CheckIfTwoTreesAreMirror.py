'''
    Given two Binary Trees, write a function that returns true if two trees are mirror of each other, 
    else false. For example, the function should return true for following input trees.

        1                   1
       / \                 / \
      3   2               2   3
         / \             / \
        5   4           4  5

    Return True
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve_rec(root1, root2):

    # valid case when we have an empty root
    if not root1 and not root2:
        return True
    
    if not root1 or not root2:
        return False

    # core of the algorithm
    # if root1.val == root2.val and root1.left == root2.right and root2.left == root1.right
    #   solve_rec(root1.left, root2.right)
    #   solve_rec(root1.right, root2.left)
    # return True
    return root1.val == root2.val and solve_rec(root1.left, root2.right) and solve_rec(root1.right, root2.left)


def main():

    root1 = Node(1)
    root1.left = Node(3)
    root1.right = Node(2)
    
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    print(solve_rec(root1, root2))




main()
