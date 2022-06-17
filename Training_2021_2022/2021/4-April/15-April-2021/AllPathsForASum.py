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
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def solve(self, root, target):
        allPaths = []
        self.backtrack(root, target, [], allPaths)
        return allPaths

    def backtrack(self, root, target, currentPath, allPaths):
        if root is None:
            return

        currentPath.append(root.val)

        if target == root.val and root.left is None and root.right is None:
            allPaths.append(list(currentPath))

        else:
            self.backtrack(root.left, target - root.val, currentPath, allPaths)
            self.backtrack(root.right, target - root.val, currentPath, allPaths)

        del currentPath[-1]

def main():
    root = Node(3)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(1)
    root.right.left = Node(2)
    #root.right.right = Node(5)
    target = 8
    solution = Solution()
    print("Tree paths with targetSum " + str(target) +
          ": " + str(solution.solve(root, target)))

main()