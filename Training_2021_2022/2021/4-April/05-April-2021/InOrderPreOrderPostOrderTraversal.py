class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def print_preorder(self, root):
        # root - left -right
        if root:
            self.res.append(root.val)
            self.print_preorder(root.left)
            self.print_preorder(root.right)
        return self.res

    def print_inorder(self, root):
        # left - root -right
        if root:
            self.print_inorder(root.left)
            self.res.append(root.val)
            self.print_inorder(root.right)
        return self.res

    def print_postorder(self, root):
        # left - right - root
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            self.res.append(root.val)
        return self.res

def main():
    root = Node(1)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(9)
    root.left.right = Node(10)
    root.right.left = Node(11)
    root.right.right = Node(15)

    solutionPre = Solution()
    solutionIn = Solution()
    solutionPos = Solution()

    preOrder = solutionPre.print_preorder(root)
    inOrder = solutionIn.print_inorder(root)
    postOrder = solutionPos.print_postorder(root)

    print(preOrder)
    print(inOrder)
    print(postOrder)

main()