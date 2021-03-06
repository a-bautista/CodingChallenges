from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            # get the current node to check if we have right or left children
            currentNode = queue.popleft()

            # if i is the last node, then save it to the results
            if i == levelSize - 1:
                result.append(currentNode)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)
    return result


def main():
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    # root.left.left.left = TreeNode(3)
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(7)
    tree.left.right = TreeNode(8)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)

    result = tree_right_view(tree)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
