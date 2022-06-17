from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.res = ""

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def count_edges(self):
        edges = 0
        for i in self.graph.keys():
            nextNodes = self.graph[i]
            while nextNodes:
                nextNodes.pop()
                edges +=1
        return edges


def main():

    g = Graph()
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)
    res = g.count_edges()
    print(res)

    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 4)
    g2.add_edge(3, 5)
    g2.add_edge(2, 5)
    g2.add_edge(2, 4)
    g2.add_edge(4, 6)
    g2.add_edge(4, 5)
    g2.add_edge(6, 5)
    res2 = g2.count_edges()
    print(res2)


main()

# time complexity: O(V + E)