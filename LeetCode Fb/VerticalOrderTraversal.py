from collections import defaultdict


def main():
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.left.left  = TreeNode(2)
    tree.left.right = TreeNode(4)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(10)

    solution = Solution()
    res = solution.solve(tree)
    print(res)
    # result = solution.print_preorder(tree)
    #print(result)

class TreeNode:
    def __init__(self,key):
        self.right = None
        self.left  = None
        self.val   = key


class Solution2:
    def traverse_preorder(self,root, level, hash_map):

        if root is None:  # end recursion
            return
        try:
            hash_map[level].append(root.val)
        except:
            # except when the level is equal to an existing list
            hash_map[level] = [root.val]

        self.traverse_preorder(root.left, level - 1, hash_map)
        self.traverse_preorder(root.right, level + 1, hash_map)

    def print_preorder(self,root):  # call the class Solution with self

        hash_map = defaultdict(list) # optimized dictionary or hash table
        level = 0
        self.traverse_preorder(root, level, hash_map)  # this is Solution.traverse_preorder


        for index, level in enumerate(sorted(hash_map)):
            #print(index, value)
            for node in hash_map[level]:
                #print(level,node)
                print('Level: {} Node: {}'.format(level, node))

        return sorted(hash_map)

from collections import deque
class Solution:
    def solve(self, root):
        if root is None:
                    return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''

if __name__ == '__main__':
    main()

    '''
        Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
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
    
    
    Code
    class TreeNode:
        def __init__(self, value):
            self.left_node   = None
            self.right_node = None
            self.key = value
              
    class Solution:
        def traverse_preorder(root, level, hash_map):
            
            if root is None: # end recursion
                return   
            try:
                hash_map[level].append(root.key)  level 0 you store hash_map[0]:[5]  
            except:    
                hash_map[level] = [root.key] don't store level 0:[5]
        
            
            traverse_preorder(root, level, hash_map[level-1])
            traverse_preorder(root, level, hash_map[level+1]
            
        
        def get_print_tree(root):
            
            # initialize the level and the data structure
            hash_map = dict()
            level = 0
            traverse_preorder(root, level, hash_map)
            
    '''

    '''
    def traverse_preorder(root, level, hash_map):

        if root is None:  # end recursion
            return
        try:
            hash_map[level].append(root.val)
        except:
            hash_map[level] = [root.val]

        traverse_preorder( root.left, level-1, hash_map)
        traverse_preorder( root.right, level+1, hash_map)


    def print_preorder(root): # call the class Solution with self

        hash_map = dict()
        level = 0
        traverse_preorder(root, level, hash_map) # this is Solution.traverse_preorder

        print(hash_map)
        for index, value in enumerate(sorted(hash_map)):
            #print(index, value)
            for i in hash_map[value]:
                print(i)
    '''