from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def rightSideView(self, TreeNode):
        
    # data structure to store the result
    result = []
      
    # test case
    if TreeNode is None:
        return result

    # data structure to use for keeping the values
    queue = deque()
    queue.append(TreeNode)
        
        
    while queue:
            
        # calculate the size of the current level
        size = len(queue)
            
        # iterate through each level
        for i in range(0,size):
                
            # retreive the current node
            node = queue.popleft()
                
            # if we get the last node from the next level
            if i == size - 1:
                result.append(node.val)
                    
            # append the left children 
            if node.left:
                queue.append(node.left)
                
            # append the right children
            if node.right:
                queue.append(node.right)
        
    return result

# Leetcode solution
#from collections import deque
#class Solution:
#    def rightSideView(self, TreeNode):
#        # data structure to store the result
#        result = []
#
#        # test case
#        if not TreeNode:
#            return result
#
#
#        queue = deque()
#        queue.append(TreeNode)
#        
#        while queue:
#            # calculate the next level            
#            size = len(queue)
#            # iterate through the next level
#            for i in range(0, size):
#                # get the value of the node from the current level
#                node = queue.popleft()
#                # if we find the last node
#                if i == size -1:
#                    results.append(node.val)
#               
#                # get the children of the current node in pre-order
#
#                if node.left: 
#                    queue.append(node.left)
#
#                if node.right:
#                    queue.append(node.right)
#
#       return result        


def main():
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    # root.left.left.left = TreeNode(3)
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(7)
    tree.left.right = TreeNode(8)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)

    result = tree_right_view(tree)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()


"""
    Time complexity: O(N)
    Space complexity: O(N)
"""