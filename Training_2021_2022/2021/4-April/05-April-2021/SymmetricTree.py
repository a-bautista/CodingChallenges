class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

# bfs
from collections import deque
def solve(root):
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
        # if the current list is not equal to its inverted then this is not a symmetric tree
        # i.e., [[1],[2,2],[3,4,4,3]] == [1], [2,2], [3,4,4,3]
        # [[1],[2,2],[3,4,4,5]] is not equal to [1], [2,2], [5,4,4,3]
        if temp != temp[::-1]:
            return False
    return True

# iteratively
def solveIteratively(root):
    if root is None:
        return True
    
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        # currentPair = stack.pop()
        # left  = currentPair[0].val
        # right = currentPair[1].val

        if left is None and right is None:
            continue
        
        if left is None or right is None:
            return False

        if left.val == right.val:
            # stack.append([currentPair[0].left, currentPair[1].right])
            # stack.append([currentPair[0].right, currentPair[1].left])
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        else:
            return False
    return True


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)

    root.right.left = Node(4)
    root.right.right = Node(3)
    res = solveIteratively(root)
    print(res)

main()