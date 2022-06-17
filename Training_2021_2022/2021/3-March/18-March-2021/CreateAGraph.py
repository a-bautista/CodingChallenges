# Use an adjacency list to represent a graph in Python
'''
            1 -> 2
            |
            v
            3 -> 4
            |
            v
            6

    adjacency_list = {
                        '1': [2, 3],
                        '2': [],
                        '3': [4, 6],
                        '4': [],
                        '6': []
                    }
    
    Consider the following graph:

    1-->2-->4-->5
        |
        v
        3

    An adjacency list can be seen as this:

    graph = Graph(5)
      0      1     2    3     4
    [None, None, None, None, None]


       0     1     2     3     4
    [None, Next, None, None, None]
            ^
            |
            2
            ^
            |
           Head

      0     1     2     3     4
    [None, Next, Next, None, None]
            ^     ^
            2     | 
            |     3
            ^     ^
            |     |
          Head   Head

      0     1     2     3     4
    [None, Next, Next, None, None]
            ^     ^
            2     | 
            |     4
            ^     ^
            |     |
          Head    3
                  |
                 Head


      0     1     2     3     4
    [None, Next, Next, None, Next]
            ^     ^           ^
            2     |           |
            |     4           5
            ^     ^           ^
            |     |           |
          Head    3          Head
        (start)   |         (start)
                 Head
                (start)
'''

class AdjacentNode:
    # similar to a LinkedList
    def __init__(self, value):
        # vertex is nothing more than the keys of the dictionary
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, value):
        self.key = value
        self.graph = [None] * self.key

    # add edges
    def add_edge(self, start, end):
        node = AdjacentNode(end)
        node.next = self.graph[start]
        self.graph[start] = node

    def print_graph(self):
        for i in range(self.key):
            print("Vertex "+ str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")
        # for i in range(self.key):
        #     print("Vertex " + str(i))
        #     temp = self.graph[i]
        #     while temp is not None:
        #         print(temp.vertex)
        #         temp = temp.next
            

def main():
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    graph.print_graph()    

main()