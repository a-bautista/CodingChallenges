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

# You need to build an adjacency list for this problem.
# Then you need to locate the target node and do a bfs to calculate the distance K to each node.

'''
             3
           /  \
          5     1
         / \   / \ 
        6   2 0   8
           / \
          7   4     


    We will create a structure like the following:

      3       5         1       Parents
     / \     / \      / | \
    5   1   6   2    3  0  8    Children

       2      6   8   0   7   4  Parents
     / | \    |   |   |   |   |
    5  7  4   5   1   1   2   2 Children

    3: [5,1]
    5: [6,2]
    1: [3,0,8]
    2: [5,7,4]
    6: [5]
    8: [1]
    0: [1]
    7: [2]
    4: [2]
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import defaultdict, deque
def solve(root, targetNode, K):
    graph = defaultdict(list)
    build_graph(root, None, graph)

    # ingredients for BFS
    visited = set()
    res = []
    queue = deque()

    # start the queue in the target node and a distance 0
    queue.append((targetNode, 0))
    while queue:

        currentNode, distance = queue.popleft()

        visited.add(currentNode)

        if distance == K:
            res.append(currentNode)

        # BFS traversal
        for adjacentNode in graph[currentNode]:

            # set to avoid infinite queue
            if adjacentNode not in visited:
                queue.append((adjacentNode, distance + 1))

    return res    

def build_graph(node, parent, graph):
    
    if not node:
        return
    
    if parent:
        # node and parent
        graph[node.val].append(parent)

    # left and right children
    if node.left:
        currentNodeLeft = node.left
        graph[node.val].append(currentNodeLeft.val)
        build_graph(currentNodeLeft, node.val, graph)

    if node.right:
        currentNodeRight = node.right
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