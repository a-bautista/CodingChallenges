
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            head, tail = self.helper(root)
            return head
        return None


    def helper(self, root):
        """Idea: Construct a DLL for each subtree, then return the head and tail. the order is in order traversal (left, root, right)."""
        head, tail = root, root

        if root.left:
            left_head, left_tail = self.helper(root.left)
            # the left child of node becomes the right node of the DLL, so we say lt.right
            left_tail.right = root   #             1  -> 2
            root.left = left_tail    # (left_tail) 1  <-> 2 (left_head)
            head = left_head         # (left_tail) 1  <-> 2 (head and left_head)

        if root.right:
            right_head, right_tail = self.helper(root.right)
            right_head.left = root  #    2 <- 3
            root.right = right_head #    (right_head) 2 <-> 3 (right_tail)
            tail = right_tail       #    (right_head) 2 <-> 3 (tail and right_tail)

        # make the reference circular
        head.left = tail
        tail.right = head
        return (head, tail)

'''
    Time complexity: O(N)
    Space complexity: O(1) we are not using any extra space
'''



'''

    

        12
       /  \
      7   24
     /   
    2
   / \
  1   3   
  
  
  
        tail ^ right head
            |
  1 <---->  2        <--->   3
  |         |                |
left_tail head ^ left_head right_tail
  
   
'''