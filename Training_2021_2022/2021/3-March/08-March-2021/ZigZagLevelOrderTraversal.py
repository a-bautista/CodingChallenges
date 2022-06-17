from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  leftToRight = True
  queue = deque()
  queue.append(root)
  while queue:
    temp = deque()
    currentSize = len(queue)
    for _ in range(currentSize):
      currentNode = queue.popleft()
      if leftToRight:
        temp.append(currentNode.val)
      else:
        temp.appendleft(currentNode.val)

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    result.append(list(temp))
    leftToRight = not leftToRight
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
