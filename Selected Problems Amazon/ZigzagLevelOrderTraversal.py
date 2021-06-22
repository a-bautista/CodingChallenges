'''

    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],

       3
      / \
     9  20
       /  \
      15   7


    Following the description of the problem, the most intuitive solution would be the BFS (Breadth-First Search)
    approach through which we traverse the tree level-by-level.
    The default ordering of BFS within a single level is from left to right. As a result, we should adjust the
    BFS algorithm a bit to generate the desired zigzag ordering.

'''

# from collections import deque
#
# class TreeNode:
#     def __init__(self,key):
#         self.right = None
#         self.left  = None
#         self.val   = key

# class Solution:
#     def zigzagLevelOrder(self, root):
#     """
#     :type root: TreeNode
#     :rtype: List[List[int]]
#     """
#     left = True
#     result = deque()
#     tmp = deque([(root, 0)])
#     while tmp:
#         node, depth = tmp.popleft()
#         if node:
#             if len(result) <= depth:
#                 result.append(deque())
#                 left = (not left)
#             if left:
#                 result[depth].appendleft(node.val)
#             if not left:
#                 result[depth].append(node.val)
#             if node.left:
#                 tmp.append((node.left, depth + 1))
#             if node.right:
#                 tmp.append((node.right, depth + 1))
#     return result

# class Solution:
#     def solve(self, root):
#         res = []
#         queue = deque()
#         queue.append(root)
#         leftToRight = True
#         while queue:
#             levelSize = len(queue)
#             current_level = deque()
#
#             for _ in (range(levelSize)):
#                 current_node = queue.popleft()
#
#                 if leftToRight:
#                     current_level.append(current_node.val)
#                 else:
#                     current_level.appendleft(current_node.val)
#
#                 if current_node.left:
#                     queue.append(current_node.left)
#                 elif current_node.right:
#                     queue.append(current_node.right)
#
#             leftToRight = not leftToRight # toggle the flag
#             res.append(list(current_level))
#         return res

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    levelSize = len(queue)
    currentLevel = deque()
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # add the node to the current level based on the traverse direction
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(list(currentLevel))
    # reverse the traversal direction
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