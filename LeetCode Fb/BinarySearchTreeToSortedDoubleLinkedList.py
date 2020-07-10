
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
        """Idea: Construct a DLL for each subtree, then return the head and tail"""
        head, tail = root, root
        if root.left:
            lh, lt = self.helper(root.left)
            lt.right = root
            root.left = lt
            head = lh
        if root.right:
            rh, rt = self.helper(root.right)
            rh.left = root
            root.right = rh
            tail = rt
        head.left = tail
        tail.right = head
        return (head, tail)