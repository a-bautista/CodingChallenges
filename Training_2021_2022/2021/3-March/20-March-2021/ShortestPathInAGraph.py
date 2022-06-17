'''
    Find the shortest path in an unweighted graph (for weighted values you need to use Dijkstra)
'''

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def find_edges(self):
        edges = 0
        for i in self.graph.keys():
            nextNodes = self.graph[i]
            for _ in nextNodes:
                edges +=1
        return edges

    def bfs(self, source, dest):
        visited = set()
        visited.add(source)
        queue = deque()
        queue.append(source)

        # you need a dictionary to keep track of the number of levels that you have traversed 
        # for each node
        distances = dict()
        distances[source] = 0

        while queue:
            vertex = queue.popleft()

            # nodes contains the adjacent lists with the nodes
            nodes = self.graph[vertex]

            for currentNode in nodes:

                # if the current node is not in the dictionary then add it with a value of 0
                if currentNode not in distances:
                    distances[currentNode] = 0

                if currentNode not in visited:
                    queue.append(currentNode)
                    visited.add(currentNode)
                    # res.append(currentNode)

                    # update the value of the current value in the adjacent list with the current vertex
                    distances[currentNode] = distances[vertex] + 1

                    if currentNode == dest:
                        return distances[currentNode]


def main():
    g1 = Graph()
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    distance = g1.bfs(0, 8)
    print(distance)

    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 5)
    g2.add_edge(2, 4)
    g2.add_edge(4, 6)
    g2.add_edge(5, 6)
    # g2.add_edge(4, 8)
    res2 = g2.bfs(1, 6)
    print(res2)


main()