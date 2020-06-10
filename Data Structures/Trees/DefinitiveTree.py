from collections import deque


def main():
    # the standard way to insert a new node in a Tree
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    # root.print_preorder(root)
    # result = root.print_traversal()
    # print(result)

    # my own way of inserting a new node in a Tree
    # you send the parent node and then the child node to send
    BST = TreeNode(2)
    BST.lookup_left_insert(BST, TreeNode(2), TreeNode(3), 'left')
    BST.lookup_right_insert(BST, TreeNode(2), TreeNode(4), 'right')
    BST.lookup_left_insert(BST, TreeNode(3), TreeNode(5), 'right')
    BST.lookup_left_insert(BST, TreeNode(3), TreeNode(1), 'left')
    BST.lookup_left_insert(BST, TreeNode(1), TreeNode(0), 'left')
    BST.lookup_left_insert(BST, TreeNode(1), TreeNode(7), 'right')
    BST.lookup_right_insert(BST, TreeNode(4), TreeNode(7), 'right')
    BST.lookup_right_insert(BST, TreeNode(4), TreeNode(12), 'left')

    result = BST.print_traversal()
    print(result)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # my own version for insertion to the left
    def lookup_left_insert(self, root, node, new_node, flag):
        '''Assume the binary tree has unique values, so you can insert either to the left or to the right.'''
        # look for the node you are looking for to insert a value on the desired node

        if root:
            if root.val == node.val: # compare values with .val
                if flag == 'right':
                    root.right = new_node
                elif flag == 'left':
                    root.left = new_node
            else:
                self.lookup_left_insert(root.left, node, new_node, flag)

    # my own version for insertion to the right
    def lookup_right_insert(self, root, node, new_node, flag):
        # look for the node you are looking for to insert a value on the desired node
        if root:
            if root.val == node.val: # compare values with .val
                if flag == 'right':
                    root.right = new_node
                elif flag == 'left':
                    root.left = new_node
            else:
                self.lookup_right_insert(root.right, node, new_node, flag)

    def simple_insert_left(self, root, new_node):
        if root:
            if root.left is None:
                root.left = new_node
            else:
                self.simple_insert_left(root.left, new_node)

    def simple_insert_right(self, root, new_node):
        if root:
            if root.right is None:
                root.right = new_node
            else:
                self.simple_insert_right(root.right, new_node)

    def insert_bst(self, root, node):
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self.insert_bst(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insert_bst(root.left, node)

    def print_preorder(self, root):
        if root:
            print(root.val)
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_traversal(root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                # add the node to the current level
                currentLevel.append(currentNode.val)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(currentLevel)

        return result


main()