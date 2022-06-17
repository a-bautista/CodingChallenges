class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def solve(self, root):
        if root is not None:
            res = self.rec_helper(root)
            if res == 0:
                root = None
            return root.val

    def rec_helper(self, root):

        if root is None:
            return 0

        sumLeft = self.rec_helper(root.left)
        sumRight = self.rec_helper(root.right)

        if sumLeft == 0:
            root.left = None

        if sumRight == 0:
            root.right = None

        return root.val + sumLeft + sumRight

    def print_preorder(self, root):
        # root - left -right
        if root:
            self.res.append(root.val)
            self.print_preorder(root.left)
            self.print_preorder(root.right)
        return self.res

    def print_inorder(self, root):
        # left - root - right
        if root:
            self.print_inorder(root.left)
            self.res.append(root.val)
            self.print_inorder(root.right)
        return self.res

    def print_postorder(self, root):
        # right - root - left
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            self.res.append(root.val)
        return self.res

def main():
    root = Node(1)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(-9)
    root.left.right = Node(2)
    root.right.left = Node(-7)
    #root.right.right = Node(0)

    solution = Solution()
    solution.solve(root)
    res = solution.print_preorder(root)
    #res = solution.solve(root)
    #res = solution.print_inorder(root)
    print(res)

main()