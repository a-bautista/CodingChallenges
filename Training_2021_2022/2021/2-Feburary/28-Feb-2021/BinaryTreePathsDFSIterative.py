class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

def solve(root):
    paths = []
    stack = [(root, str(root.val))]

    if root is None:
        return paths

    while stack:

        current_node, curren_path = stack.pop()

        if not current_node.left and not current_node.right:
            paths.append(curren_path)

        if current_node.left:
            stack.append((current_node.left, curren_path+'->'+str(current_node.left.val)))

        if current_node.right:
            stack.append((current_node.right, curren_path+'->'+str(current_node.right.val)))

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

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''