'''
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

        3       -> 1
       / \
      9   20    -> 2
         /  \
        15   7

    return 2

'''

class Node:
    def __init__(self, key):
        self.val   = key
        self.left  = None
        self.right = None


from collections import deque
def solve(root):
    queue = deque()
    distance = 0
    queue.append(root)

    if not root:
        return distance

    while queue:
        distance += 1
        level = len(queue)
        for _ in range(level):
            currentNode = queue.popleft()
            if currentNode:
                if currentNode.left is None and currentNode.right is None:
                    return distance
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)


def main():
    node = Node(3)
    node.left = Node(9)
    node.right = Node(20)
    node.right.right = Node(7)
    node.right.left = Node(15)
    res = solve(node)
    print(res)

main()

