'''
    Same approach as bfs level order traversal
    Find the minimum depth of a binary tree. The minimum depth is the number of nodes along 
    the shortest path from the root node to the nearest leaf node.

            1
           / \
          2   3 <-- min depth = 2
         / \
        4   5    

            1
           / \
          2   3 
         / \   \
        4   5  10 <-- min depth = 3
       /
      12

            1
           / \
          2   3 
         / \   \
        4   5  10 <-- min depth = 3
       /
      12

     1
    / \
   2   3 <- min depth = 2

    I store each level of nodes in a Q
    if there are not any children nodes, then we have reached th min depth
    

    queue = [(1)] and minDepth = 0
    queue = [(2,3)] and minDepth = 1
    currentNode = queue.popleft()
    if currentNode.left is None and currentNode.right is None:
        return minDepth

'''

from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve(root):
    queue = deque()
    distance = 0
    queue.append(root)
    
    if not root:
        return distance +1

    while queue:
        distance +=1
        level = len(queue)
        for _ in range(level):
            currentNode = queue.popleft()
            if currentNode:
                if currentNode.left is None and currentNode.right is None:
                    return distance
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #root.right.left = Node(12)
    #root.right.left.left = Node(125)
    res = solve(root)
    print(res)

main()

        #     1
        #    / \
        #   2   3 <-- min depth = 2
        #  / \
        # 4   5  

#      10    1
#     / \
#    5   15   2
#  /     / \
# 1     12  16 3
#       /
#      125 