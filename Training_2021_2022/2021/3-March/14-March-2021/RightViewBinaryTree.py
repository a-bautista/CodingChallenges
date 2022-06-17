'''
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the 
    nodes you can see ordered from top to bottom.

    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

'''
class Node:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None

from collections import deque
def solve(root):

    # edge cases
    if not root:
        return 

    res = []
    queue = deque()
    queue.append(root)
    #res.append(root.val)
    while queue:
        currentLevel = len(queue)
        temp = []
        for _ in range(currentLevel):
            currentNode = queue.popleft()
            temp.append(currentNode.val)

            # Get the left children
            if currentNode.left:
                queue.append(currentNode.left)

            # Get the right children
            if currentNode.right:
                queue.append(currentNode.right)
        
        # Get the last value from the list
        res.append(temp[-1])
    return res

'''
    1. I want to traverse the tree with BFS to get the nodes at each level.
    2. In a list, get only the last node value from the current level
    3. Get the remianing nodes to the queue for BFS traversal
    4. Return the list with results
'''

def main():

    '''
            1
           / \
          2   3
           \   \
            5   4
    res = 1,3,4
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(4)
    res = solve(root)
    print(res)

main()