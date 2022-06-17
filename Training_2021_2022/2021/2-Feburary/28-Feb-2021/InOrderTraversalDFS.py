class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def solve(root):
    stack = []
    res = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        if not stack:
            return res

        current_node = stack.pop()
        res.append(current_node.val)
        root = current_node.right


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(5)
    res = solve(root)
    print(res)

main()