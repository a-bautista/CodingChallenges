from collections import deque
class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

def solve(root):
    res = []
    queue = deque()
    queue.append(root)

    if root is None:
        return res

    while queue:
        currentLevel = len(queue)
        temp = []

        for _ in range(currentLevel):

            currentNode = queue.popleft()
            temp.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        res.append(temp)
    return res

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(5)
    res = solve(root)
    print(res)

main()

