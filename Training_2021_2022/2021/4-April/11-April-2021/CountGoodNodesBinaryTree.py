'''
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no 
    nodes with a value greater than X.

    Return the number of good nodes in the binary tree.

    Example 1:

            3
           / \
          1   4
         /   / \
        3   1   5

        output: 4
        3 which is the root is always a good node
        4 is greater than 3, so it is also a good node
        5 is greater than 3 and 4, so it is also a good node
        3 is also a good node because it is greater than 1      
'''
class Node:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None

from collections import deque
def solve(root):
    ans = 0
    queue = deque()
    queue.append((root, float('-inf')))

    while queue:
        currentNode, maxVal = queue.popleft()

        # if the current node has a greater value than the max value of the current node
        if currentNode.val >= maxVal:
            ans+=1

        if currentNode.left:
            queue.append((currentNode.left, max(maxVal, currentNode.val)))

        if currentNode.right:
            queue.append((currentNode.right, max(maxVal, currentNode.val)))

    return ans

def main():
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.left = Node(3)
    root.right.left = Node(1)
    root.right.right = Node(5)
    res = solve(root)
    print(res)
    
    '''
            3
           / \
          1   4
         /   / \
        3   1   5
    '''

main()