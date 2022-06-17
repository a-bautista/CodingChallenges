'''
    Given a binary tree, return the vertical order traversal of its nodes' values. 
    (ie, from top to bottom, column by column).
    If two nodes are in the same row and column, the order should be from left to right.
    
    Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
   
   -2   -1  0   1    2 
            5
         /    \
        3       8
       / \     /  \
    2      4  7    10  
   
   [2],[3], [5,4,7],[8],[10]

   I want to createt the following data structure:

   {
       -2: [2]
       -1: [3]
        0: [5,4,7]
        1: [8]
        2: [10]
   }

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque, defaultdict

def solve(root):
    queue = deque()
    queue.append((root,0))
    leftMost = 0
    rightMost = 0
    dd = defaultdict(list)

    while queue:
        currentNode, currentLevel = queue.popleft()
        if currentNode:
            dd[currentLevel].append(currentNode.val)
            leftMost = min(leftMost, currentLevel)
            rightMost = max(rightMost, currentLevel)
            queue.append((currentNode.left, currentLevel -1))
            queue.append((currentNode.right, currentLevel +1))

    return [dd[x] for x in range(leftMost, rightMost+1)]

def main():
    root = Node(3)
    root.left = Node(9)
    #root.left.left = Node(4)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    res = solve(root)
    print(res)

main()
        