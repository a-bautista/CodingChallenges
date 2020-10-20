'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example:

tree t
        3
      /  \
     4   5
   / \
  1   2


subtree s

    4
  /  \
 1    2

answer is True because the structure is the same

tree t
        3
      /  \
     4   5
   / \
  1   2


subtree s

    4
  /  \
 1    2
       \
        3

answer is False because s is not the contained in any part of t

What means identical trees?
Two trees are considered to be identical if the root values and their left and right subtrees are identical.

Approach
The pre-order traversal (middle, left, right) can be used to compare the root, then the left and right subtrees
I can store the root, left and right values in a list, and then I can do a comparison of these two lists and verify if
the elements of the subtree s are contained in tree t.

Which approach is better? Recursive or iterative?
Recursive because trees are traversed in recursive order

Our trees only accept integers, right? Yes

result = comparison(t, s)
print(result)

def comparison(tree, subtree)
    val_first_tree = []
    val_second_tree = []
    pre_order(tree, val_first_tree)
    pre_order(tree, val_second_tree)


    # how to check if two lists are identical (you can use Counter)

    if collections.Counter(val_first_tree) == collections.Counter(val_second_tree):
        return True
    else:
        return False


def pre_order(tree, l):
    # if there's not an empty tree
    if tree:
       l.append(str(tree.val))
       pre_order(tree.left,l)
       pre_order(tree.right,l)
    else:
       l.append('Null')

return True or False if they are the same

'''

import collections

def main():
    tree = Node(3) # root
    insert(tree, Node(4))
    insert(tree, Node(5))
    insert(tree, Node(1))
    insert(tree, Node(2))

    subtree = Node(1)
    insert(subtree, Node(3))
    #insert(subtree, Node(2))

    #print_preorder(tree)
    result = comparison(tree, subtree)
    print(result)

class Node:
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.val = key

def insert(tree, node):
    # elements greater than a node go to the right
    if tree.val < node.val:
        # if there's an empty value to the right of the root node, you can insert the new node
        if tree.right is None:
            tree.right = node # I insert a node, then I get left and a right children

        # in case there's not an empty value to the right, then do deep 1 level (recursion)
        else:
            insert(tree.right, node) # get the value of the right and insert the new node

    # elements lower than a node go to the left
    else:
        # if there's an empty value to the left of the root node, you can insert the new node
        if tree.left is None:
            tree.left = node # I insert a node, then I get left and a right children
        else:
            insert(tree.left, node)

def print_preorder(tree):

    if tree:
        print(tree.val)
        print_preorder(tree.left)
        print_preorder(tree.right)

def pre_order(tree, l):
    # if there's not an empty value in the tree
    if tree:
       l.append(str(tree.val))
       pre_order(tree.left,l)
       pre_order(tree.right,l)
    else:
       l.append('Null')

def comparison(tree, subtree):
    val_first_tree = []
    val_second_tree = []
    pre_order(tree, val_first_tree)
    pre_order(subtree, val_second_tree)
    print(val_first_tree)
    print(val_second_tree)

    # how to check if a list is contained in another list (you can use Counter)
    n1 = len(val_first_tree)
    n2 = len(val_second_tree)

    # determine if the sublist is contained in the main list
    if n1>n2:
        return any(val_second_tree == val_first_tree[i:i+n2] for i in range(n1-n2+1))

    #if collections.Counter(val_first_tree) == collections.Counter(val_second_tree):
    #    return True
    #else:
    #    return False

if __name__ == '__main__':
    main()