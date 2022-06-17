'''
    We are given a Binary Search Tree(BST) and a node number N. 
    We have to find the node with the nth highest value.
    # this is resolved with inverse in-order traversal (R-Center-L)

                    100
                    / \
                  50    200
                  / \   / \
                 25 75 125 350     

    Highest node is 350
    2nd2nd2nd highest node is 200
    3rd3rd3rd highest node is 125
    4th4th4th highest node is 100
    5th5th5th highest node is 75

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    
    def findNHighestNode(self, root, n):
        # base case
        if not root:
            return None
        
        rightBranch = self.findNHighestNode(root.right, n)
        
        if rightBranch is not None:
            return rightBranch
        
        self.count +=1
        if n == self.count:
            return root.val

        leftBranch = self.findNHighestNode(root.left, n)        
        if leftBranch is not None:
            return leftBranch
        return None

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.right.right = Node(16)
    root.right.left = Node(12)
    solution = Solution()
    res = solution.findNHighestNode(root, 2)
    #res = solve(root)
    print(res)

main()

    
    
'''
    Time complexity: O(log*n) because it is a binary search tree
    Space complexity: O(h)
'''