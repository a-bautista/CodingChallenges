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
       / \
      2   3
     /\   \
    4 5    7

    Use BFS to do a level order traversal, add children to the bfs queue,
    until we met the first empty node.

    For a complete binary tree,
    there should not be any node after we met an empty one.



    2nd approach:
	1. bfs and the queue finally should have all the leaves including null
	2. for a complete binary tree, there should not be any node after we met a null node in the final level

	e.g.1
				1
			2		3
		4 5	 6
	queue = [null, null, null, null, null, null, null]
	parent = 3		4	 4		5	 5		6	 6
	so it is complete

	e.g.2
				1
			2		3
		4 5	 		6
	queue = [null, 6, null, null, null, null]
	parent = 3	   3	4	4	   5	5

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%


'''

#from collections import deque
# def isCompleteTree(root):
#     bfs = [root]
#     i = 0
#     while bfs[i]:
#         bfs.append(bfs[i].left)
#         bfs.append(bfs[i].right)
#         i += 1
#     return not any(bfs[i:])

class Solution:
    def isCompleteTree(self, root):
        q = [root]
        while q[0] != None:
            # this pop(0) simulates the q.popleft() from the queue
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)

        while len(q) > 0 and q[0] == None:
            # this pop(0) simulates the q.popleft() from the queue
            q.pop(0)
        # this indicates that if there's no element in the queue then we have a complete binary tree
        return len(q) == 0

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''