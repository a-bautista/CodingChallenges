class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def solve(root):
    paths = []
    stack = [(root, str(root.val))]
    while stack:
        currentNode, currentPath = stack.pop()

        if not currentNode.left and not currentNode.right:
            paths.append(currentPath)
        
        if currentNode.left:
            stack.append((currentNode.left, currentPath+"->"+str(currentNode.left.val)))

        if currentNode.right:
            stack.append((currentNode.right, currentPath+"->"+str(currentNode.right.val)))
    
    return paths
        


def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    res = solve(root)
    print(res)

main()