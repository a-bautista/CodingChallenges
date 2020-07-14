'''
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
    of every node never differ by more than 1.

    Example:

    Given the sorted linked list: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5




'''




# Recursively form a BST out of linked list from l --> r

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedListToBST(self,head):

        # Get the size of the linked list first
        size = self.findSize(head)

        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal (left, root, right).
            # Recursively from the left half until you get a Null
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            # to convert it into TreeNode
            node = TreeNode(head.val)

            node.left = left

            # move onto the next element of the linked list
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)


    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

'''
    Time complexity: O(N)
    Space complexity: O(Log(N))
'''