class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary

def main():
    root = Node(100)
    root.left = Node(50)
    root.right = Node(200)
    root.left.left = Node(25)
    root.left.right = Node(60)
    root.left.left.left = Node(10)
    root.left.right.right = Node(70)
    root.right.right = Node(350)
    root.right.right.right = Node(400)
    solution = Solution()
    res = solution.boundaryOfBinaryTree(root)
    print(res)

main()