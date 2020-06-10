from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque() # use a queue to store the elements of the tree
  queue.append(root) # bring the first node of the tree
  while queue:
    levelSize = len(queue)  # how many nodes are in this level?
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft() # empty the queue for storing the next element
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left) #bring the left nodes of level from above
      if currentNode.right:
        queue.append(currentNode.right) #bring the right nodes of level from above

    result.append(currentLevel)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()