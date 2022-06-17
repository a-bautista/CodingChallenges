#   12
#  /  \
# 8   43
#      \
#      90

class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

from collections import deque
def solve(node):
    queue = deque()
    queue.append(node)
    res = []

    while queue:
        currentSize = len(queue)
        temp = []
        for _ in range(currentSize):
            currentNode = queue.popleft()
            temp.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        res.append(temp)
    return res

def main():
    root = Node(12)
    root.left = Node(8)
    root.right = Node(43)
    root.right.right = Node(17)
    res = solve(root)
    print(res)

main()