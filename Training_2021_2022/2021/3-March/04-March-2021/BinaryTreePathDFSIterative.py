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

def dfs_iterative(root):
    stack = []
    res = []
    stack.append((root, str(root.val)))

    while stack:
        current_node, current_path = stack.pop()

        # if you have reached the deepest leaf without any child, then attach the current path which contains the results
        if not current_node.left and not current_node.right:
            res.append(current_path)

        if current_node.left:
            stack.append((current_node.left,current_path+"->"+str(current_node.left.val)))
        if current_node.right:
            stack.append((current_node.right,current_path+"->"+str(current_node.right.val)))
    return res

    # stack= [(root, str(root.val))]
    # paths = []
    
    # while stack:
    #     current_node, current_path = stack.pop()
        
    #     if not current_node.left and not current_node.right:
    #         paths.append(current_path)
            
    #     if current_node.left:
    #         stack.append((current_node.left, current_path+'->'+str(current_node.left.val)))
        
    #     if current_node.right:
    #         stack.append((current_node.right, current_path+'->'+str(current_node.right.val)))
    
    # return paths

def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    res = dfs_iterative(root)
    print(res)

main()