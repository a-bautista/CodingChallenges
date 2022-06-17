class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

def solve(root):
    stack = []
    previous_node = float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        current_node = stack.pop()
        if previous_node >= current_node.val:
            return False

        previous_node = current_node.val
        root = current_node.right
    return True

def main():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    res = solve(root)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''