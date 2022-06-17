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
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque
def solve(root):
    queue = deque()
    queue.append(root)
    minDepth = 0
    while queue:
        minDepth+=1
        size = len(queue)
        for _ in range(size):
            currentNode = queue.popleft()
            if not currentNode.right and not currentNode.left:
                return minDepth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return -1

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.right.right = Node(16)
    root.right.left = Node(12)
    res = solve(root)
    print(res)

main()

