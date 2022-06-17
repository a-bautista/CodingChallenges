'''
    Given the root of a binary tree, return the sum of values of its deepest leaves. 
    
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

            1
          /  \
         2    3
        / \    \
       4   5    6
      /          \       
     7            8
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
    res = []
    while queue:
        temp = []
        size = len(queue)
        for _ in range(size):
            currentNode = queue.popleft()
            if currentNode:
                temp.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        res.append(temp)
    return sum(res[-1])


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    root.left.left.left = Node(7)
    root.right.right.right = Node(8)

    res = solve(root)
    print(res)

main()