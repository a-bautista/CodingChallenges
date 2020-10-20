from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def solve(root):
    result = []
    if root is None:
        return result

    queue = deque([root])
    while (queue):
        levelSize = len(queue)
        current_level = []

        for _ in range(levelSize):
            # you save the current values of each level from the queue in the current level
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    res = solve(root)
    print(res)


main()