'''
    1. Define the flag for the switch of leftToRight and the queue for getting the values of the Tree
    2. Define the loops for getting the values of each node

'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
def solve(TreeNode):
    res = []
    queue = deque()
    queue.append(TreeNode)
    # define the flag
    leftToRight = True

    while queue:
        # store the results from the zigzag in this queue
        other_queue = deque()
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # get the values through zigzag
            if leftToRight:
                other_queue.append(currentNode.val)
            else:
                other_queue.appendleft(currentNode.val)

            # append the children from nodes
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        # do the switch of the flag
        leftToRight = not leftToRight
        res.append(list(other_queue))
    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(solve(root))


main()