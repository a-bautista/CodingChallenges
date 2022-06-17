class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def solve(root):
    stack = []
    previous = float('-inf')
    while root or stack:
        while root:
            stack.append(root)
            # move the root to the left
            root = root.left
        
        lastNode = stack.pop()

        # compare the last value inserted with the previous node
        if previous>=lastNode.val:
            return False

        previous = lastNode.val
        root = lastNode.right
    return True

def main():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    res = solve(root)
    print(res)

main()