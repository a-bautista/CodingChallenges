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
   
   
   
   
    Requirements:
    
    1. We need to traverse the tree in a pre-order traversal (traverse_preorder) 
    2. Hash map for storing the keys of the tree level paired to the  list values:
    
        {
         -2:[2],
         -1:[3],
         0:[5,4,7],
         1:[8],
         2:[10]
         }
    
    3. At the end you need to print them in descending order.
    
    In the worst case, the time for inserting each value in the hashmap is O(n).
    Space complexity is O(n) because we depend on the size of the tree. 
    
    
    How the algorithm works?
            
    level  0 of node 5 you store hash_map[0]:[5]
    level -1 of node 3 you store hash_map[-1]:[3]
    level -2 of node 2 you store hash_map[-2]:[2] # end recursion
    
    
    level -1 of node 3 (right) hash_map[-1+1=0] you store hash_map[0].append(4) # [0]:[5,4] end recursion
    level 0 of node 5 (right) hash_map[0+1] you store hash_map[1].append(8) 
    level 0 of node 8 (left) hash_map[1-1=0] you store [0]:[5,4,7] 
    level -1 of node 8 # end recursion
    level 2 of node 5 (right) hash_map[1+1=2] you store [10]
    
    
    you store hash_map[-1+1=0] don't store [3]
    level 1 of node 3 you store hash_map[0+1] 

'''
from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None

def solve2(root):
    
    if not root:
        return []

    dd = defaultdict(list)
    queue = deque()
    maxLevel = minLevel = 0
    queue.append((root,0))

    while queue:
        currentNode, level = queue.popleft()

        if currentNode:
            
            dd[level].append(currentNode.root)
            # min and max Levels are only used for tracking where you will start getting the minimum and max values
            # when you print the values
            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)
            queue.append((currentNode.left, level - 1))
            queue.append((currentNode.right, level + 1))

    return [dd[x] for x in range(minLevel, maxLevel + 1)]

def solve(root):
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.root)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

def main():

    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(4)
    root.right = Node(9)
    root.right.right = Node(10)
    res = solve2(root)
    print(res)

main()


