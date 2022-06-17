from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.res = ""

    def add_node(self, start, end):
        self.graph[start].append(end)

    def solve(self):
        visited = set()
        rec_visited = set()
        keys = self.graph.keys()

        for node in keys:
            if self.detect_cycle(node, visited, rec_visited):
                return True
        return False

    def detect_cycle(self, node, visited, rec_visited):

        # cycle found
        if (node in rec_visited):
            return True

        if (node in visited):
            return False

        visited.add(node)
        rec_visited.add(node)

        # use the condition from below to avoid the insertion of new keys at runntime for the defaultdict, so
        # you avoid problems when traversing it
        if node in self.graph.keys():
            nextNodes = self.graph[node]
            #print(nextNodes)

            for childNode in nextNodes:
                if (self.detect_cycle(childNode, visited, rec_visited)):
                    return True

            rec_visited.discard(node)
            #rec_visited[node] = False
            return False


def main():
    g1 = Graph()
    g1.add_node(0, 1)
    #g1.add_node(2, 99)
    g1.add_node(1, 2)
    g1.add_node(1, 3)
    g1.add_node(3, 4)
    res = g1.solve()
    print(res)


main()