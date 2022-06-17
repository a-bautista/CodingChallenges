'''
    Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
    (i.e., from left to right, level by level from leaf to root).

         3
        / \
       9   20
          /  \
         15  7

    [[15,7],[9,20],[3]]

'''

from collections import deque
class Node:
    def __init__(self, val):
        self.key   = val
        self.right = None
        self.left  = None

def sol_bfs_level_2(node):
    res = deque()
    queue = deque()
    queue.append(node)

    if not node:
        return res

    while queue:
        level = len(queue)
        temp = []
        for _ in range(level):
            current_node = queue.popleft()
            temp.append(current_node.key)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        res.appendleft(temp)
    return res


def main():
    node = Node(1)
    node.left  = Node(2)
    node.right = Node(3)
    node.left.right = Node(4)

    # node.right.left  = Node(4)
    node.right.right = Node(5)
    sol = sol_bfs_level_2(node)
    print(sol)

main()