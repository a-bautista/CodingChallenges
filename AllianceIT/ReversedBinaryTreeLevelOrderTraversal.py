from collections import deque

class TreeNode:
    def __init__(self, value):
        self.root = value
        self.left, self.right = None, None


def reverse_level_order_traversal(node):

    res_queue = deque()
    if not node:
        return res_queue

    queue = deque([node])
    while queue:
        size = len(queue)
        current_level = []
        for _ in range(size):
            current_node = queue.popleft()
            current_level.append(current_node.root)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        res_queue.appendleft(current_level)
    return res_queue

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    res = reverse_level_order_traversal(root)
    print(res)

main()