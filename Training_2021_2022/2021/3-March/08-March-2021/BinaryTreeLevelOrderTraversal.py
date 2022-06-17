class Node:
  def __init__(self, data):
    self.data  = data
    self.right = None
    self.left  = None

from collections import deque
def level_order_traversal(root):
  
  res = []
  queue = deque()
  queue.append(root)
  while queue:
    temp = []
    levelSize = len(queue)
    for _ in range(levelSize):
      currentNode = queue.popleft()
      temp.append(currentNode.data)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    res.append(temp)
  return res

def main():
    root = Node(6)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(8)

    res = level_order_traversal(root)
    print(res)

main()