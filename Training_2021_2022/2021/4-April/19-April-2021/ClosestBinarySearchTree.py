'''
        Given a non-empty binary search tree and a target value, find the value in the BST that 
        is closest to the target.

        Note:
            Given target value is a floating point.
            You are guaranteed to have only one unique value in the BST that is closest to the target.
        
        Example:

        Input: root = [4,2,5,1,3], target = 3.714286

             4
            / \
           2   5
          / \
         1   3

        Output: 4
        We cannot have duplicates.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def solve(root, target):
    queue = deque()
    queue.append(root)
    minDiff = float('inf')

    while queue:
        level = len(queue)
        for _ in range(level):
            currentNode = queue.popleft()
            if currentNode:
                # you need the absolute value to get the distance between the current node and target node
                currDiff = abs(float(currentNode.val) - target)
                if currDiff < minDiff:
                    res = currentNode.val
                    # store the minimum difference
                    minDiff = currDiff
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
    return res

def main():

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    res = solve(root, 3.75)
    print(res)

    '''
             4
            / \
           2   5
          / \
         1   3
    '''

main()

