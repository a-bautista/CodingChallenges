class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

# The logic behind this is that the in-traverse goes from left->middle->right.
# Stack is LIFO

def inorderTraversal(root):
    res, stack = [], []
    while True:
        # 1. We start getting all the nodes from center to left into the stack.
        # 4. We continue again getting the nodes until the stack is empty, then we give back the res result.
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        # 2.Once we get to the bottom of the left nodes, we pop the node and insert it into the res list.
        node = stack.pop()
        res.append(node.val)
        # 3.If the left node contains any right node, then we make it the root variable but this node will be
        # inserted at the very end of the stack.
        root = node.right

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = inorderTraversal(root)
    print(res)

main()