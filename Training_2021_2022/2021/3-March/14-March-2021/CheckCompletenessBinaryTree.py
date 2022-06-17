'''
    Given a binary tree, determine if it is a complete binary tree.

     1
    / \
    2   3
    /\  /
    4 5 6

    In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
    are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


    The above binary tree is True because it fulfills the completeness because all of the very last nodes
    are to the very left.

    The following tree doesn't satisfy the requirement of completeness because there is 1 node that
    is not to the very left.

       1
     /   \
    2     3
   / \   /  \
   4  5  N   7
   Output: False

    Explanation:
    All the nodes should be to the left side but here we will end up with the following situation:

    Children    None   None     None  None     None  None   None  None
    Parent           4               5             None          7

    We don't want to end in the situation where there was one parent as a None
    
          1
        /   \
       2     3
      / \   /  \
     4   5  6  None
    /
   8
    output: False
    Children       8   None     None  None     None  None   None  None   
    Parent           4               5             6            None  

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def solve(root):
    '''
        Do a BFS to get each level in the tree.
        When you add the left nodes, determine if there's a None or not. if there's  none then the Tree is
        not complete.
    '''
    
    # Base Case: An empty tree is complete Binary tree 
    if root is None: 
        return True

    queue = deque()
    queue.append(root)
    res = []
    flag = False
    isAboveNodeNull = False

    while queue:
        currentSize   = len(queue)
        isCurrentNodeNull = False

        for _ in range(currentSize):
            currentNode = queue.popleft()
            if currentNode is not None:
                if isCurrentNodeNull or isAboveNodeNull:
                    return False
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                isCurrentNodeNull = True
        # in case there's one more deep level and the last node from the current level was Null
        isAboveNodeNull = isCurrentNodeNull
    return True


def main():
    root       = Node(1)
    root.left  = Node(2)
    root.right = Node(3)
    root.left.left   = Node(4)
    root.left.right  = Node(5)
    root.right.right = Node(7)
    res = solve(root)
    print(res)

#       1
#     /  \
#    2    3
#   / \   /\
#  4   5 N  7
# return False because you have a None in one left child branch

#       1
#     /  \
#    2    3
#   / \   /\
#  4   N 6  7
# return False 

#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   N
# return True because you have values in all left nodes


main()

