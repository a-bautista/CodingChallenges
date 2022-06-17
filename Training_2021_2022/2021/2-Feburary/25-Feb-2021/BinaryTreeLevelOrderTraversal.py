class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

        #   12
        #  /  \
        # 8   43
        #      \
        #      90

from collections import deque
def solve(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        temp = []
        levelSize = len(queue)
        for _ in range(levelSize):
            current_node = queue.popleft()
            temp.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        res.append(temp)
    return res

def main():
    root = TreeNode(12)
    root.left = TreeNode(8)
    root.right = TreeNode(43)
    root.right.right = TreeNode(17)
    res = solve(root)
    print(res)

main()