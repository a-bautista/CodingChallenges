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

def solve(root, targetNode, distanceK):
    graph = defaultdict(list)
    build_graph(root, None, graph)

    # ingredients for BFS
    queue = deque()
    visited = set()
    res = []

    # you start traversing from the target node
    queue.append((targetNode, 0))

    while queue:
        currentNode, currentDist = queue.popleft()
        visited.add(currentNode)

        if currentDist == distanceK:
            res.append(currentNode)

        for adjacentNode in graph[currentNode]:
            if adjacentNode not in visited:
                queue.appendleft((adjacentNode, currentDist + 1))

    return res

# convert the tree into a graph
def build_graph(node, parent, graph):

    if not node:
        return 

    if parent:
        graph[node.val].append(parent)

    if node.left:
        currentNodeLeft = node.left
        # parent --> child
        graph[node.val].append(currentNodeLeft.val)
        build_graph(currentNodeLeft, node.val, graph)

    if node.right:
        currentNodeRight = node.right
        # parent --> child
        graph[node.val].append(currentNodeRight.val)
        build_graph(currentNodeRight, node.val, graph)



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
    #solution = Solution()
    res = solve(root, 5, 2)
    print(res)

main()