'''
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
    Return the root node reference (possibly updated) of the BST.

    Basically, the deletion can be divided into two stages:

        Search for a node to remove.
        If the node is found, delete the node.

    Follow up: Can you solve it with time complexity O(height of tree)?

    Delete node 3

                5
               / \
              3   6
             / \   \
            2   4   7 

    Then

                5
               / \
              4   6
             /     \
            2       7 

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        if not root: 
            return None
        
        if root.val == key:
            if not root.right: 
                # when we return return root.left of the root, we are providing a None value, which deletes the given target
                return root.left
            
            if not root.left: 
                # when we return root.right of the root, we are providing a None value, which deletes the given target
                return root.right
            
            if root.left and root.right:
                temp = root.right
                # get the max value of the temp.left
                while temp.left: 
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root

def main():

    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)

    solution = Solution()
    res = solution.deleteNode(root, 2)
    print(res)

main()

'''
    Time complexity: O(h)
    space complexity: 

    https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained
'''