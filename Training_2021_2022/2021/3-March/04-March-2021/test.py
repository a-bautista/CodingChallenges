'''
       1
      /  \
     4   10
        /  \
       2    12

    1->4
    1->10->2
    1->10->12
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def solve(root):
    res   = []
    stack = []
    stack.append((root, str(root.val)))

    while stack:

        currentNode, currentPath = stack.pop()
        if not currentNode.left and not currentNode.right:
            res.append(currentPath)
        
        if currentNode.left:
            stack.append((currentNode.left, currentPath+"->"+str(currentNode.right.val)))

        if currentNode.right:
            stack.append((currentNode.right, currentPath+"->"+str(currentNode.right.val)))
    
    return res

def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    res = solve(root)
    print(res)
    

main()