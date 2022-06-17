'''
    Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of 
    all the node values of each path equals ‘S’. Please note that the paths can start or 
    end at any node but all paths must follow direction from parent to child (top to bottom).
'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root,targetSum):
  return count_paths_recursive(root,targetSum, [])


def count_paths_recursive(currentNode,targetSum, currentPath):
  if currentNode is None:
    return 0

  # add the current node to the path
  currentPath.append(currentNode.val)
  pathCount, pathSum = 0, 0
  # find the sums of all sub-paths in the current path list
  for i in range(len(currentPath)-1, -1, -1):
    pathSum += currentPath[i]
    # if the sum of any sub-path is equal to 'S' we increment our path count.
    if pathSum ==targetSum:
      pathCount += 1

  # traverse the left sub-tree
  pathCount += count_paths_recursive(currentNode.left,targetSum, currentPath)
  # traverse the right sub-tree
  pathCount += count_paths_recursive(currentNode.right,targetSum, currentPath)

  # remove the current node from the path to backtrack
  # we need to remove the current node while we are going up the recursive call stack
  del currentPath[-1]

  return pathCount


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()

'''
    The time complexity of the above algorithm is (N^2) in the worst case, where ‘N’ is the total number of 
    nodes in the tree. This is due to the fact that we traverse each node once, but for every node, 
    we iterate the current path. The current path, in the worst case, can be O(N) (in the case of a skewed tree). 
    But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., 
    O(logN)O(logN)O(logN). So the best case of our algorithm will be O(NlogN)O(NlogN)O(NlogN).


    Space complexity: O(N)

'''