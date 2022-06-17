'''
    Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p 
    and value q in the tree.

    The distance between two nodes is the number of edges on the path from one to the other.

            3
           / \
          5    1
        /  \  / \     
       6   2  0  8
          / \
         7   4

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
    Output: 3
    Explanation: There are 3 edges between 5 and 0: 5-3-1-0.     
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def findDistance(self, root, p, q):
        lca = self.findLCA(root, p, q)
        print(lca.val)
        return self.findTargetBFS(lca, p) + self.findTargetBFS(lca, q)
        
    def findLCA(self, root, p, q):
        
        if not root:
            return None
        
        if root.val in (p,q):
            return root
        
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        
        if left and right:
            return root
        return left or right
    
        
    def findTargetBFS(self, lca, target):
        queue = deque()
        queue.append((lca,0))
        
        while queue:
            currentNode, dist = queue.popleft()
            if currentNode.val == target:
                return dist
            if currentNode.left:
                queue.append((currentNode.left, dist+1))
            if currentNode.right:
                queue.append((currentNode.right, dist+1))
def main():

    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    p = 6
    q = 2

    solution = Solution()
    res = solution.findDistance(root, p, q)
    print(res)

main()