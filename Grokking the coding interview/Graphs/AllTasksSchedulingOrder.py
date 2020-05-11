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

        # stack to print all topological orders
        stack = []

        self.print_all_topological_orders(in_degree, queue, stack)

    def print_all_topological_orders(self, in_degree, queue, stack):

        if queue:
            for vertex in queue:
                stack.append(vertex)
                queueForNextCall = deque(queue)
                queueForNextCall.remove(vertex)

                for child in self.graph[vertex]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queueForNextCall.append(child)

                self.print_all_topological_orders(in_degree, queueForNextCall, stack)
                stack.remove(vertex)

                for child in self.graph[vertex]:
                    in_degree[child] += 1

        if len(stack) == len(in_degree):
            print(stack)


def main():
    g = Graph(5)
    g.addEdge(4, 2)
    g.addEdge(4, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 1)


    solution = g.topologicalSort()
    print(solution)


main()

"""
    Problem:
        Given the tasks and prerequisistes, find all the possible ordering of tasks.
        Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
        Output: 
            1) [3, 2, 0, 1]
            2) [3, 2, 1, 0]
        
    Theory:
        Again, we can use the Kahn algorithm with backtrack. 


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