'''
    A mother vertex in a graph G =(V,E) is a verex v such that all other
    vertices in G can be reached by a path from v. Find the mother vertex
    in the directed graph.

         3
        / \
       v   v
       0   1
            \
             v
             2 
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_adjacent_node(self, start, end):
        self.graph[start].append(end)

    def find_mother_vertex(self):

        numOfVertices = 0
        for i in self.graph.keys():
            numOfVertices = self.dfs(i)
            if numOfVertices == len(self.graph.keys()):
                return i
        return -1

    def dfs(self, source):

        visited = set()
        verticesReached = 0
        totalVertices = len(self.graph.keys())
        stack = []
        stack.append(source)

        # visited.add(source)
        while stack:
            currentNode = stack.pop()

        if currentNode in self.graph.keys():
            nextNodes = self.graph[currentNode]
            for i in nextNodes:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
                    verticesReached += 1
        return verticesReached + 1


# class Solution2:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def build_graph(self, edges):
#         for A, B in edges:
#             self.graph[A].append(B)
#             self.graph[B].append(A)

    
#     def find_mother_vertex(self, edges):
#         self.build_graph(edges)
#         # print(self.graph)
#         for i in self.graph.keys():
#             numOfVertices = self.dfs(i)
#             if numOfVertices == len(self.graph.keys())-1:
#                 return i
#         return -1


#     def dfs(self, source):
#         visited = set()
#         verticesReached = 0
#         totalVertices = len(self.graph.keys())
#         stack = []
#         stack.append(source)

#         # visited.add(source)
#         while stack:
#             currentNode = stack.pop()

#         if currentNode in self.graph.keys():
#             nextNodes = self.graph[currentNode]
#             for i in nextNodes:
#                 if i not in visited:
#                     stack.append(i)
#                     visited.add(i)
#                     verticesReached += 1
#         return verticesReached + 1

def main():
    graph = Graph()
    graph.add_adjacent_node(0, 1)
    graph.add_adjacent_node(1, 2)
    graph.add_adjacent_node(3, 0)
    graph.add_adjacent_node(3, 1)
    graph.add_adjacent_node(4, 0)
    graph.add_adjacent_node(4, 1)
    graph.add_adjacent_node(4, 2)
    # solution = Solution2()
    # #edges = [[3,0],[3,1],[1,2]]
    edges = [[0,1],[1,2],[3,0],[3,1],[4,0],[4,1],[4,2]]
    # res = solution.find_mother_vertex(edges)
    # print(res)
    res = graph.find_mother_vertex()
    print(res)


main()