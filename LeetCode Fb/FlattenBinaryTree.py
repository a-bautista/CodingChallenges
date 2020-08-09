from collections import deque

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    result = root.print_traversal()
    print(result)
    flatten = root.flattenTree(root)
    result2 = flatten.print_traversal()
    flatten.print_preorder(root)



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

    def flattenTree(self, root):

        # edge case: handle null scenario
        if root is None:
            return None

        # when you hit the end of the tree, return the node
        if not root.left and not root.right:
            return root

        # flatten to the left subtree
        left_tail = self.flattenTree(root.left)
        # Recursively flatten the right subtree
        right_tail = self.flattenTree(root.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side anymore.

        if left_tail:
            # at the very end of the tail_left.right, you will add the right children of the root
            left_tail.right = root.right
            # the root will have the contents of the left_tail which also contains the previously added nodes from root.right
            root.right = root.left
            # we don't need the contents of the root.left, so make it None
            root.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return right_tail if right_tail else left_tail

main()

"""
    Given a binary tree, flatten it to a linked list in-place.
    For example, given the following tree:

         1
        / \
       2   5
      / \   \
     3   4   6
  

    The output should be:

    1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

    Another example:
         1
        / \
       2   5
      / \  /\
     3   4 2 6
    /\  /\
   5  7 9 10
   
   1
    \
     2
      \
       3
        \
         5
          \
           7
            \
             4
              \
               9
                \
                 10
    
     
    Algorithm:
        1. Start traversing the tree from the left side. 
        2. Reach the bottom of the left side tree (DFS).
        3. If there's a right node on the very bottom, append it to the end of the left side (tail_left).
        4. Go back to verify if the previous nodes have children to the right. (Recursion)
            4.1. Append the left nodes to the tail_left (recursion). 
            4.2. Append the right nodes to the tail_left. 
        5. Traverse the right side until you hit the end. 
        6. If there's a left node on the very bottom, append it to the right side (right_tail)
        7. Go back to verify if the previous nodes have children to the left. 
            7.1. Append the left nodes to the tail_right.
            7.2. Append the right nodes to the tail_right. 
        8. Join the left_tail to the right_tail. 
   
   Time complexity: O(N)
   Space complexity: O(N)   
             
"""