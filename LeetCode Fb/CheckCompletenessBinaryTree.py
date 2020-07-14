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

        1
       / \
      2   3
     /\   \
    4 5    7

    This tree doesn't satisfy the requirement of completeness because there is 1 node that
    is not to the very left.

    Use BFS to do a level order traversal, add children to the bfs queue,
    until we met the first empty node.

    For a complete binary tree,
    there should not be any node after we met an empty one.

'''

#from collections import deque
def isCompleteTree(root):
    bfs = [root]
    i = 0
    while bfs[i]:
        bfs.append(bfs[i].left)
        bfs.append(bfs[i].right)
        i += 1
    return not any(bfs[i:])

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''