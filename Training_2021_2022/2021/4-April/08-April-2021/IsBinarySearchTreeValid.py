class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve(root):
    stack = []
    previousNode = float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        lastNode = stack.pop()
        if previousNode >= lastNode.val:
            return False
        
        previousNode = lastNode.val
        root = lastNode.right
    return True

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.right.right = Node(16)
    root.right.left = Node(12)
    
    res = solve(root)
    print(res)

main()


    # if the previous value is greater than the current node then return false
