from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def check_path(self, source, dest):

        visited = set()
        res = False

        if source == dest:
            return True

        for vertex in self.graph.keys():
            res = self.helper_dfs(visited, vertex, dest)
        return res

    def helper_dfs(self, visited, vertex, destination):
        visited.add(vertex)
        # stack.append(node)

        if vertex == destination:
            return True

        if vertex in self.graph.keys():
            for ele in self.graph[vertex]:
                if ele not in visited:
                    self.helper_dfs(visited, ele, destination)
        return False

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
    res = g1.check_path(3, 0)
    print(res)

main()