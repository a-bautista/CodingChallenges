# from collections import deque
#
#
# def is_scheduling_possible(tasks, prerequisites):
#   sortedOrder = []
#   if tasks <= 0:
#     return False
#
#   # a. Initialize the graph
#   inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
#   graph = {i: [] for i in range(tasks)}  # adjacency list graph
#
#   # b. Build the graph
#   for prerequisite in prerequisites:
#     parent, child = prerequisite[0], prerequisite[1]
#     graph[parent].append(child)  # put the child into it's parent's list
#     inDegree[child] += 1  # increment child's inDegree
#
#   # c. Find all sources i.e., all vertices with 0 in-degrees
#   sources = deque()
#   for key in inDegree:
#     if inDegree[key] == 0:
#       sources.append(key)
#
#   # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
#   # if a child's in-degree becomes zero, add it to the sources queue
#   while sources:
#     vertex = sources.popleft()
#     sortedOrder.append(vertex)
#     for child in graph[vertex]:  # get the node's children to decrement their in-degrees
#       inDegree[child] -= 1
#       if inDegree[child] == 0:
#         sources.append(child)
#
#   # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
#   # will not be able to schedule all tasks
#   return len(sortedOrder) == tasks
#
#
# def main():
#   print("Is scheduling possible: " +
#         str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
#   print("Is scheduling possible: " +
#         str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
#   print("Is scheduling possible: " +
#         str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))
#   print("Is scheduling possible: " +
#         str(is_scheduling_possible(6, [[5, 2], [5, 0], [4,0], [4, 1], [2, 3], [3, 1]])))
#
# main()

from collections import defaultdict
from collections import deque

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # The function to do Topological Sort.

    def topologicalSort(self):

        # Create a vector to store indegrees of all vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of vertices. This step takes O(V+E) time
        # in_degree [0, 0, 0]
        # [0,1], [1,2], [2,0]

        # i in self.graph -> 0
        # j in self.graph -> 1 because 0 is the parent vertex
        # [0, 1, 0] because in_degree[j] += 1

        # i in self.graph -> 1
        # j in self.graph -> 2 because 1 is the parent vertex
        # [0, 1, 1] because in_degree[j] += 1

        # i in self.graph -> 2
        # j in self.graph -> 0 because 2 is the parent vertex
        # [1, 1, 1] because in_degree[j] += 1

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create a queue and enqueue all vertices with indegree 0. If there isn't then,
        # we have a cyclic dependency.
        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        visited_v = 0

        # Create a vector to store result (A topological ordering of the vertices)
        #top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue) and add it to topological order
            u = queue.popleft()
            #top_order.append(u)

            # Iterate through all neighbouring nodes of dequeued node u and decrease
            # their in-degree by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)
            visited_v += 1

        # Check if there was a cycle when visited_v is not equal to the total number of vertices.
        if visited_v != self.V:
            return False
        else:
            return True

def main():
    g = Graph(6)
    g.addEdge(0, 4)
    g.addEdge(1, 4)
    g.addEdge(3, 2)
    g.addEdge(1, 3)

    solution = g.topologicalSort()
    print(solution)

main()

"""
    Problem:
        There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite 
        tasks which need to be completed before it can be scheduled. Given the number of tasks 
        and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
        
        Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
        Output: true
        
        Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
        before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
    
    Theory:
        The Kahn's algorithm can be used to solve this problem and it states that:
        
        1. All paths must be of finite length S.
        2. There's the path S that goes from u ( source ) to v (destination).
        3. Since S is the longest path, there cannot be any incoming edge to 'u' and no 
            outgoing edge from 'v', that is, indegree(u)=0 and outdegree(v)=0.
       
            
    Algorithm:
        1. Compute the in-degree for each vertex and initialize the count of visited nodes to 0.
        2. Pick all the vertices with in-degree 0 and add them to a queue. 
        3. Remove a vertex from the queue and:
            3.1. Increment the count of visited nodes by 1.
            3.2. Decrease the in-degree by 1 from all child nodes of the picked vertex. 
            3.3. If one of the child nodes has an in-degree = 0 then add it to the queue.
        4. Repeat step 3 until the queue is empty.
        5. If count of visited nodes is not equal to the number of vertices then it is not
            possible to assign tasks due to cyclic dependency.  
        
    Time complexity: 
        O(V+E) where v is the number of tasks and e is the number of prerequisites. 
    
    Space complexity:
        O(V+E) since we are storing all of the prerequisites for each task in adjacency list. 
        
"""