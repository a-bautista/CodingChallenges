from collections import deque
class TreeNode:
    def __init__(self, value):
        self.root = value
        self.right, self.left = None, None


def zigzag_traversal(root):
    result = []
    if not root:
        return result
    queue = deque([root])
    left_to_right = True

    while queue:
        size = len(queue)
        current_level = deque()

        for _ in range(size):
            current_node = queue.popleft()

            if left_to_right:
                current_level.append(current_node.root)
            else:
                current_level.appendleft(current_node.root)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    res = zigzag_traversal(root)
    print(res)

main()