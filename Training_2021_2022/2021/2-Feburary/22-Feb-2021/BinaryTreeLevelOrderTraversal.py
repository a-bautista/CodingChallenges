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
def solve(TreeNode):
    res = []
    queue = deque()
    queue.append(TreeNode)
    while queue:
        currentLevel = [] # stores the nodes from the current level
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()  # get the nodes from the queue
            currentLevel.append(currentNode)
            # get the children of the nodes
            if currentNode.left:
                queue.append(currentNode.left)
            else:
                queue.append(currentNode.right)
        res.append(currentLevel)
    return res

def main():
    root = TreeNode(12)
    root.left = TreeNode(8)
    root.right = TreeNode(43)
    root.right.right = TreeNode(17)
    res = solve(root)
    print(res)

main()
