'''
    We are given a binary tree (with root node root), a target node, and an integer value K.

    Return a list of the values of all nodes that have a distance K from the target node.  
    The answer can be returned in any order.

    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

             3
           /  \
          5     1
         / \   / \ 
        6   2 0   8
           / \
          7   4               

    Output: [7,4,1]

    Explanation: 
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.

'''

from collections import defaultdict, deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:        
    def distanceK(self, root, target,  K):
        g = defaultdict(list)
        vis, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        self.convert_into_graph(root, None, g)
        print(g)
        q.append((target, 0))
        
        while q:
            n, distance = q.popleft()
            vis.add(n)
            
            if distance == K:
                res.append(n)
            
            # adjacency list traversal
            for adjacentNode in g[n]:
                if adjacentNode not in vis:
                    q.append((adjacentNode, distance + 1)) 
                
        return res
    
    def convert_into_graph(self, node, parent, g):
        # To convert the tree into graph we need to know who is the parent
        if not node:
            return
        
        if parent:
            g[node.val].append(parent)
            
        if node.right:
            currentValRight = node.right
            g[node.val].append(currentValRight.val)
            self.convert_into_graph(node.right, node.val, g)
        
        if node.left:
            currentValLeft = node.left
            g[node.val].append(currentValLeft.val)
            self.convert_into_graph(node.left, node.val, g)


def main():
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(8)
    solution = Solution()
    res = solution.distanceK(root, 5, 2)
    print(res)

main()