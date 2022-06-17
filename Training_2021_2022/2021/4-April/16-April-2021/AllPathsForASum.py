'''
    Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the
    node values of each path equals ‘S’.

    
	S: 12
    Output: [[1, 7, 4], [1, 9, 2]]
    Explanation: 
    Here are the two paths with sum '12':1 -> 7 -> 4 and 1 -> 9 -> 2

            1
           / \
          7   9
        /  \ / \
       4   5 2  7  
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def solve(self, root, targetSum):
        allPaths = []
        self.backtrack(root, targetSum, [], allPaths)
        return allPaths

    def backtrack(self, root, targetSum, currentPath, allPaths):
        
        if root is None:
            return 

        currentPath.append(root.val)

        if root.val == targetSum and root.left is None and root.right is None:
            allPaths.append(list(currentPath))    

        else:
            self.backtrack(root.left, targetSum - root.val, currentPath, allPaths)
            self.backtrack(root.right, targetSum - root.val, currentPath, allPaths)

        del currentPath[-1]

def main():
    root = Node(3)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(1)
    root.right.left = Node(2)
    #root.right.right = Node(5)
    targetSum = 8
    solution = Solution()
    print("Tree paths with targetSum " + str(targetSum) +
          ": " + str(solution.solve(root, targetSum)))

main()