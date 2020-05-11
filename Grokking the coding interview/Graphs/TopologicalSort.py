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

        # print one topological order
        sortedOrder = []

        # edge case when no vertices are given
        if self.V <= 0:
            return sortedOrder

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

        # Create a queue and enqueue all vertices with indegree 0.
        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            vertex = queue.popleft() # remove the source node
            sortedOrder.append(vertex) # add the source node to the final result
            for child in self.graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        # edge case to determine cyclic dependency
        if len(sortedOrder) != self.V:
            return []

        return sortedOrder


def main():
    g = Graph(4)
    g.addEdge(3, 2)
    g.addEdge(3, 0)
    g.addEdge(2, 1)
    g.addEdge(2, 0)


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