class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None    

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.findLCA(root, p, q)
    
    def findLCA(self, root, p, q):
        
        if not root:
            return None
        
        if root.val == p or root.val == q:
        #if root.val in (p,q):
            return root
        
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        
        if left and right:
            return root
        return left or right


def main():
    # root = Node(3)
    # root.left = Node(5)
    # root.right = Node(1)
    # root.left.left = Node(6)
    # root.left.right = Node(2)
    # root.right.left = Node(0)
    # root.right.right = Node(8)
    p = 10
    q = 10
    
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    #root.left.right.left = Node(7)
    #root.left.right.right = Node(4)
    root.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.right.right.right = Node(10)

    sol = Solution()
    res = sol.lowestCommonAncestor(root, p, q)
    #res = findLCA(root, p, q)
    print(res.val)

main()