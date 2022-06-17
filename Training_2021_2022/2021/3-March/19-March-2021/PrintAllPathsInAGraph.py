from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.minDist = float('inf')
        self.allPaths = ""

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def print_all_paths(self, source, dest):
        
        visited = set()
        #visited.add(source)
        paths = []
        self.helper_print(source, dest, visited, paths)
        return self.allPaths

    def helper_print(self, source, dest, visited, paths):

        visited.add(source)
        paths.append(source)

        if source == dest:
            self.allPaths+=str(paths)

        elif source in self.graph.keys():
            for node in self.graph[source]:
                if node not in visited:
                    self.helper_print(node, dest, visited, paths)
        
        paths.pop()
        visited.discard(source)


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
    res = g1.print_all_paths(0, 8)
    print(res)

main()