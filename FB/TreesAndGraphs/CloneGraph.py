"""
 if there is an undirected edge between node A and node B, the graph representation
 for it would have a directed edge from A to B and another from B to A. After all,
 an undirected graph is a set of nodes that are connected together, where all the edges
 are bidirectional. How else would you say that A could be reached from B and B could be
 reached from A?

 A--B is undirected which means it can go from A-->B or A<---B.

"""

from collections import defaultdict, deque

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def clone_graph(self):

        cloned_graph = []

        if self.V <= 0:
            return cloned_graph

        visited = {}
        queue = deque()
        queue.append(self.graph[3])
        print(queue)

        while (queue):
            n = queue.popleft()



# from collections import deque
# class Solution(object):
#
#     def cloneGraph(self, node):
#         """
#         :type node: Node
#         :rtype: Node
#         """
#
#
#         if not node:
#             return node
#
#         # Dictionary to save the visited node and it's respective clone
#         # as key and value respectively. This helps to avoid cycles.
#         visited = {}
#
#         # Put the first node in the queue
#         queue = deque([node])
#         # Clone the node and put it in the visited dictionary.
#         visited[node] = Node(node.val, [])
#
#         # Start BFS traversal
#         while queue:
#             # Pop a node say "n" from the from the front of the queue.
#             n = queue.popleft()
#             # Iterate through all the neighbors of the node
#             for neighbor in n.neighbors:
#                 if neighbor not in visited:
#                     # Clone the neighbor and put in the visited, if not present already
#                     visited[neighbor] = Node(neighbor.val, [])
#                     # Add the newly encountered node to the queue.
#                     queue.append(neighbor)
#                 # Add the clone of the neighbor to the neighbors of the clone node "n".
#                 visited[n].neighbors.append(visited[neighbor])
#
#         # Return the clone of the node from visited.
#         return visited[node]

def main():
    g = Graph(4)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(1, 4)
    g.addEdge(4, 1)

    g.clone_graph()


main()