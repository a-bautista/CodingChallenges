'''

    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
    level by level).

    #    3
    #  /  \
    # 9   20
    #     / \
    #    15  7

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

'''
from collections import deque
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def bfs_level_order_traversal(root):

    res = []
    queue = deque()
    queue.append(root)

    while queue:

        size = len(queue)
        temp = []

        for _ in range(size):
            current_node = queue.popleft()
            temp.append(current_node.val)

            # insert into the queue, the values from the left and right of the current node for the next iteration
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # append the values from the nodes left and right
        res.append(temp)
    return res


def main():
    node = Node(3)
    node.left  = Node(9)
    node.right = Node(20)
    node.right.left  = Node(15)
    node.right.right = Node(7)
    res = bfs_level_order_traversal(node)
    print(res)


main()

'''
1. Get the root node and insert it into a queue.
2. While there are values in the queue, get the current size of the values in the queue.
3. Traverse the current level by getting the current node and then making sure you have left and right nodes.
4. If you have left and right nodes, add them to the queue
5. Add the current node values to the main array

'''