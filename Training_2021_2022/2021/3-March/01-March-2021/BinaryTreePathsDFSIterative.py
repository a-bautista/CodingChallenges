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
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

def solve_dfs_paths(root):
    stack = [(root, str(root.val))]
    res = []

    while stack:
        current_node, current_path = stack.pop()

        if not current_node.left and not current_node.right:
            res.append(current_path)

        if current_node.left:
            stack.append((current_node.left, current_path+"->"+str(current_node.left.val)))
            
        if current_node.right:
            stack.append((current_node.right, current_path+"->"+str(current_node.right.val)))
    return res


def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    res = solve_dfs_paths(root)
    print(res)

main()