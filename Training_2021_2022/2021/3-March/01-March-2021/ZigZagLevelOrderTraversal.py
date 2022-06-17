# class Node:
#     def __init__(self, key):
#         self.val = key
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
def solve(TreeNode):
    res = []
    leftToRight = True
    queue = deque()
    queue.append(TreeNode)

    while queue:

        another_queue = deque()
        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()
            if leftToRight:
                another_queue.append(current_node.val)
            else:
                another_queue.appendleft(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        leftToRight = not leftToRight
        res.append(list(another_queue))
    return res

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    res = solve(root)
    print(res)


main()