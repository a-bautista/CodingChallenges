'''
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.

         1
        / \
       2   3
        \   \
         5   4
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def sol_right_side(node):

    res = []
    queue = deque()
    queue.append(node)

    if not node:
        return res

    while queue:
        level = len(queue)
        temp = []

        for _ in range(level):
            current_node = queue.popleft()
            temp.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        res.append(temp[-1])

    return res

def main():
    node = Node(1)
    node.left  = Node(2)
    node.right = Node(3)
    node.left.right = Node(4)

    # node.right.left  = Node(4)
    node.right.right = Node(5)
    sol = sol_right_side(node)
    print(sol)

main()