'''
    Same approach as bfs level order traversal
    Find the max depth of a binary tree. 

            1
           / \
          2   3 
         / \
        4   5   <-- max depth = 2 

            1
           / \
          2   3 
         / \   \
        4   5  10 
       /
      12         <-- max depth = 4
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
    maxDepth = 0
    while queue:
        maxDepth+=1
        size = len(queue)
        for _ in range(size):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return maxDepth

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.right.right = Node(16)
    root.right.left = Node(12)
    root.right.left.left = Node(125)
    res = solve(root)
    print(res)

main()

