'''
    Given a binary tree, populate an array to represent the averages of all of its levels.
'''
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

from collections import deque
def solve(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        tempAverage = []
        for _ in range(size):
            currentNode = queue.popleft()
            tempAverage.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        res.append(sum(tempAverage)/size)
    return res

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.right.right = Node(16)
    root.right.left = Node(12)
    res = solve(root)
    print(res)

main()