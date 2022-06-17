class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# too complex
from collections import deque
def solve(root):
    if not root:
        return []
    
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        tempQ = deque()
        for _ in range(size):
            currentNode = queue.popleft()
            if currentNode:
                tempQ.appendleft(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        res.append(list(tempQ))
    return res

# time complexity: O(n)
# space complexity: O(n)
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

from collections import deque
def bfsInvertTree(root):
    
    queue = deque()
    queue.append(root)
    # iterate over the Q
    while queue:
        # extract the nodes
        currentNode = queue.popleft()
        if currentNode:
        # append the nodes of the new updated nodes
            currentNode.left, currentNode.right = currentNode.right, currentNode.left
            # check if there's a node and if so then make the node.right = node.left and viceversa
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return root


def main():
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    res = bfsInvertTree(root)
    print(res)
    
main()