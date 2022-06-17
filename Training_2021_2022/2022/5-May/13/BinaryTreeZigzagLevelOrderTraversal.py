'''
    Given the root of a binary tree, return the zigzag level order 
    traversal of its nodes' values. (i.e., from left to right, then
    right to left for the next level and alternate between).

         3
        / \
       9   20
           / \
          15  7


    Output: [[3], [20, 9], [15, 7]]

'''

from logging.config import valid_ident
from multiprocessing.dummy import current_process


class Node:
    def __init__(self, val):
        self.key   = val
        self.right = None
        self.left  = None

from collections import deque
def bfs_zigzag(node):

    res = []
    queue = deque()
    queue.append(node)
    to_left = True

    while queue:
        level = len(queue)
        temp_queue = deque()

        for _ in range(level):
            current_node = queue.popleft()

            if to_left:
                temp_queue.append(current_node.key)
            else:
                temp_queue.appendleft(current_node.key)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        to_left = not to_left
        res.append(list(temp_queue))
    return res


def main():
    node = Node(3)
    node.left  = Node(9)
    node.right = Node(20)
    node.right.left  = Node(15)
    node.right.right = Node(7)
    sol = bfs_zigzag(node)
    print(sol)

main()