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

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def find_paths(self, root, targetSum):
        allPaths = []
        self.find_paths_recursive(root, targetSum, [], allPaths)
        return allPaths


    def find_paths_recursive(self, currentNode, targetSum, currentPath, allPaths):
        if currentNode is None:
            return

        # add the current node to the path
        currentPath.append(currentNode.val)

        # if the current node is a leaf and its value is equal to targetSum, save the current path
        if currentNode.val == targetSum and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
        else:
            # traverse the left sub-tree
            self.find_paths_recursive(currentNode.left, targetSum -
                                currentNode.val, currentPath, allPaths)
            # traverse the right sub-tree
            self.find_paths_recursive(currentNode.right, targetSum -
                                currentNode.val, currentPath, allPaths)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currentPath[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  targetSum = 23
  solution = Solution()
  print("Tree paths with targetSum " + str(targetSum) +
        ": " + str(solution.find_paths(root, targetSum)))


main()
