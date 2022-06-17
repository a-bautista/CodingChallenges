from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.res = ""
    
    def add_adjacent_node(self, start, end):
        self.graph[start].append(end)

    def print_graph(self):
        for i in range(len(self.graph.keys())):
            print("Current index or vertex: "+ str(i))
            currentNode = self.graph[i]
            print(currentNode)
    
    def bfs(self):
        queue = deque()
        visited = set()
        res = ""
        queue.append(0)
        visited.add(0)

        while queue:
            vertex = queue.popleft()
            for value in self.graph[vertex]:
                if value not in visited:
                    res+=str(value)
                    visited.add(value)
                    queue.append(value)
        return res

def main():

    graph = Graph()
    graph.add_adjacent_node(0, 1)
    graph.add_adjacent_node(1, 2)
    graph.add_adjacent_node(2, 3)
    graph.add_adjacent_node(2, 4)
    graph.add_adjacent_node(3, 6)
    graph.add_adjacent_node(4, 5)
    graph.print_graph()
    res=graph.bfs()
    print(res)


main()
