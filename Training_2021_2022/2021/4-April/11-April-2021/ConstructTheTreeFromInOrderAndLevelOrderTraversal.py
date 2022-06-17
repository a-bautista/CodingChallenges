'''
    Given inorder and level-order traversals of a Binary Tree, construct the Binary Tree. 
    Following is an example to illustrate the problem.

    Input: Two arrays that represent Inorder
       and level order traversals of a 
       Binary Tree
    
    in[]    = {4, 8, 10, 12, 14, 20, 22};
    level[] = {20, 8, 22, 4, 12, 10, 14};

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def build_tree(inOrder, levelOrder):
    if inOrder:
        inIndex = 0
        node = None
        for i in range(0, len(levelOrder)):
            if levelOrder[i] in inOrder:
                node = Node(levelOrder[i])
                inIndex = inOrder.index(levelOrder[i])
                break
        
        if not inOrder:
            return node

        # construct the left and right binary tree
        node.left  = build_tree(levelOrder, inOrder[0:inIndex])
        node.right = build_tree(levelOrder, inOrder[inIndex + 1:len(inOrder)])
        return node

def print_inorder(root):
    if node is None:
        return []

    print_inorder(node.left)
    print_inorder(node.val)    
    print_inorder(node.right)


def main():
    levelorder = [20, 8, 22, 4, 12, 10, 14]
    inorder = [4, 8, 10, 12, 14, 20, 22]
 
    # ino_len = len(inorder)
    root = build_tree(levelorder, inorder)
    print_inorder(root)

main()