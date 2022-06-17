class Node:
    def __init__(self,key):
        self.val = key
        self.left, self.right = None, None

def solve(root):
    stack = []
    previous = float('-inf')

    while stack or root:
        # 1. We start getting all the nodes from center to left into the stack.
        while root:
            stack.append(root)
            root = root.left
        # 2. We assign root as the last inserted element into the stack
        root = stack.pop()

        # 3.If the last inserted element is less than the previous value then this is not BST
        if previous>= root.val:
            return False

        # 4. Set the previous variable to the value of root
        previous = root.val

        # 5. Get the values from right children
        root = root.right
    return True

def main():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    res = solve(root)
    print(res)

main()