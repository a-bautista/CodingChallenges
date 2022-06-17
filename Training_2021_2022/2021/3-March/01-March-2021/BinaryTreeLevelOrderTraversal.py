class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

from collections import deque
def solve(root):
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        currentSize = len(queue)
        temp = []

        for _ in range(currentSize):
            current_node = queue.popleft()
            temp.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        res.append(temp)
    return res


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)

    root.right.left = Node(4)
    root.right.right = Node(3)
    res = solve(root)
    print(res)

main()