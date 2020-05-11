from collections import defaultdict

class Graph:

  # build the graph to hold the adjacency lists and vertices
  def __init__(self, vertices):
    self._graph =defaultdict(list) # adjacency lists will be contained
    self._v = vertices             # number of vertices

  # append an edge
  def addEdge(self, u, v):
    self._graph[u].append(v)


  def helper_topologicalSort(self, v, visited, stack):

      # mark the current vertex as visited
      visited[v] = True

      # recursion for all the vertices adjacent to the current vertex
      # graph = [5,2], [5,0], [4,0], [4,1], [3,1], [2,3]
      # visited = [True, False, False, False, False, False]
      #              0     1      2      3     4       5

      # traverse each adjacency list to find its children
      # i will start with the number that is tied to the parent vertex
      # i.e., [2,3] v is 2 and i will become 3
      for i in self._graph[v]:
          # if the current vertex has not been visited
          if visited[i] == False:
              # get the children of the current vertex
              self.helper_topologicalSort(i, visited, stack)

      # add the visited vertex to the stack at index 0 to print the list in reverse order (as a stack)
      stack.insert(0,v)

  # function to do topological sort. Use recursion with the helper function
  def topologicalSort(self):

      # Create the list to set the vertices as not visited
      visited = [False] * self._v
      stack = []

      for i in range(self._v):
          if visited[i] == False:
              self.helper_topologicalSort(i, visited, stack)
      return stack


def main():
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    result = g.topologicalSort()

    print("Following is a Topological Sort of the given graph")
    print(result)

main()


"""
    Problem:
    
        Given a directed graph, find the topological ordering of its vertices.
        
        Input: Vertices = 4, Edges = [[3, 2], [3, 0], [2, 0], [2, 1]]
        Output: These 2 results are valid (only 1 of these needs to be printed).
                1) 3, 2, 0, 1
                2) 3, 2, 1, 0
        
        Input: Vertices = 7, Edges = [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
        Output: 
              1) 5, 6, 3, 4, 0, 1, 2
              2) 5, 6, 4, 3, 0, 1, 2
              3) 6, 5, 4, 3, 0, 1, 2
              ....
              
              Use the topologicalOrder.java class from the Udemy Kotlin course to find all the possible
              values. 
    
    Theory:
                
                   3   ------> source
                 /    \ 
                2----> 0---> sink
                |
                1----------> sink
                
        The values 3, 2, 1, 0 are called vertices.
        The connections from each value are called edges.
        The value 3 is called the source because it doesn't have any incoming edges.
        The values 1 and 0 are called the sinks because these do not have outgoing edges.
        The vertex 2 has 1 in-degree (one incoming edge).
        The vertex 0 has 2 in-degree (two incoming edges). 
    
    
    Algorithm:
        1. Get all the children of each value in adjacent lists. 
        2. Traverse each adjacent list with DFS but instead of printing each vertex in the first
           place, store each value in a stack if the value has not been visited and if there
           are no more children vertices. 
        3. Create a hashmap or list for each vertex to determine which one has already been visited.
        4. Once all the vertices have been visited, the initial vertices will be stored in the stack 
           and then it will be printed.
   
    Time complexity:
    O(V+E) where V is the number of vertices and E is the number of edges.
    
    Space complexity:
    O(V+E) since we are storing all vertices and edges in adjacency lists.
         
        More details at https://www.geeksforgeeks.org/topological-sorting/       
"""