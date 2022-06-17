'''
            1 -> 2
            |
            v
            3 -> 4
            |
            v
            6

    adjacency_list = {
                        '1': [2, 3],
                        '2': [],
                        '3': [4, 6],
                        '4': [],
                        '6': []
                    }
    
    Consider the following graph:

    1-->2-->4-->5
        |
        v
        3

    An adjacency list can be seen as this:

    graph = Graph(5)
      0      1     2    3     4
    [None, None, None, None, None]


       0     1     2     3     4
    [None, Next, None, None, None]
            ^
            |
            2
            ^
            |
           Head

      0     1     2     3     4
    [None, Next, Next, None, None]
            ^     ^
            2     | 
            |     3
            ^     ^
            |     |
          Head   Head

      0     1     2     3     4
    [None, Next, Next, None, None]
            ^     ^
            2     | 
            |     4
            ^     ^
            |     |
          Head    3
                  |
                 Head


      0     1     2     3     4
    [None, Next, Next, None, Next]
            ^     ^           ^
            2     |           |
            |     4           5
            ^     ^           ^
            |     |           |
          Head    3          Head
        (start)   |         (start)
                 Head
                (start)
'''
from collections import defaultdict
 
# This class represents a
# directed graph using adjacency
# list representation
 
class Graph:
 
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        # variable to store the results of the traversal
        self.res = ""
        # you cannot get the length from here, needs to be done at runtime
        # self.keys = len(self.graph.keys())
 
    # function to add an edge to graph
    # start: u
    # end : v
    def addEdge(self, start, end):
        self.graph[start].append(end)
 
    def print_graph(self):
        for i in range(len(self.graph.keys())):
            print("Index or Vertex: ", i)
            currentNode = self.graph[i]
            print(currentNode)

    # A function used by DFS
    def dfs_helper(self, v, visited):
 
        # Mark the current node as visited
        visited.add(v)
        self.res += str(v)
 
        # Recur for all the elements (neighbor) that are under the 
        # current vertex v adjacent to
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_helper(neighbour, visited)
    
 
    def dfs(self):
        # Create a set to store all visited vertices
        visited = set()
        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one. list(self.graph) converts the keys in iterable objects
        for vertex in list(self.graph):
            if vertex not in visited:
                self.dfs_helper(vertex, visited)
        return self.res

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 6)
g.addEdge(4, 5)
g.print_graph()
#g.addEdge(3, 3)
print("Following is Depth First Traversal")
res = g.dfs()
print(res)