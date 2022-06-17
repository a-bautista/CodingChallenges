class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve(root):
    diameter = 0
    def rec(root):

        nonlocal diameter
        if not root:
            return 0

        left = rec(root.left)
        right = rec(root.right)

        # determine if the left + right branch are bigger than the current diameter
        diameter = max(left + right, diameter)

        # return the left or right branch + 1 which includes the parent node
        return max(left, right) + 1
    rec(root)
    return diameter


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.right = Node(3)
    res = solve(root)
    print(res)

main()