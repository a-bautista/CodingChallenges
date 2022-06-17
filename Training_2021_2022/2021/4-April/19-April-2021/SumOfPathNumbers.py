'''
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. 
    Find the total sum of all root-to-leaf numbers.

         1
        / \
       2   3

    12 + 13 = 25    

    DFS 
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def solve(self, root):
        self.allPaths = []
        self.backtrack([], root)
        return sum(self.allPaths)

    def backtrack(self, currentPath, root):

        currentPath.append(str(root.val))
        if root.left is None and root.right is None:
            res = "".join(currentPath)
            self.allPaths.append(int(res))
        else:
            self.backtrack(currentPath, root.left)
            self.backtrack(currentPath, root.right)
        
        # eliminate the last node
        del currentPath[-1]


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    solution = Solution()
    res = solution.solve(root)
    print(res)
    

main()