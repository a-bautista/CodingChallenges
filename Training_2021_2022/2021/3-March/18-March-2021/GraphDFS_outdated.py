class AdjacentNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, value):
        self.keys   = value
        self.graph = [None] * self.keys


    def add_edge(self, start, end):
        node         = AdjacentNode(end)
        node.next    = self.graph[start]
        self.graph[start] = node


    def print_graph(self):
        for i in range(self.keys):
            print("Index or Vertex: " + str(i))
            currentNode = self.graph[i]
            while currentNode is not None:
                print(currentNode.vertex)
                currentNode = currentNode.next


    # def dfs_traversal_helper(self, graph, source, numericSource, visited):
    #     result = ""
    #     stack = []
    #     stack.append(source)
    #     visited[numericSource] = True
    #     nextNode = None
    #     while stack:
    #         currentNode = stack.pop()
    #         #print(type(currentNode))
    #         #print(currentNode.vertex)
    #         if currentNode is not None:
    #             result += str(currentNode.vertex)
    #             nextNode = currentNode.next
    #         while nextNode:
    #             #if visited[int(nextNode.vertex)] is False:
    #             # add the current node
    #             stack.append(nextNode)
    #             # move onto the next vertex for getting the
    #             stack.append(self.graph[nextNode.vertex])
    #             #visited[int(nextNode.vertex)] = True
    #             if self.graph[nextNode.vertex]:
    #                 visited[self.graph[nextNode.vertex]] = True
    #             nextNode = nextNode.next
    #     return result, visited

    def dfs_traversal_helper(self, graph, source, numericSource, visited):
        result = ""
        stack = []
        stack.append(source)
        visited[numericSource] = True
        nextNode = None
        while len(stack)!=0:
            currentNode = stack.pop()
            if currentNode is not None:
                result += str(currentNode.vertex)
                #nextNode = self.graph[nextNode.vertex]
                nextNode = currentNode.next
            while nextNode:
                if visited[int(nextNode.vertex)] is False:
                    # add the current node
                    stack.append(nextNode)
                    # move onto the next vertex for getting the
                    # stack.append(self.graph[nextNode.vertex])
                    # visited[int(nextNode.vertex)] = True
                    if self.graph[nextNode.vertex]:
                        visited[int(nextNode.vertex)] = True
                        #visited[self.graph[nextNode.vertex]] = True
                nextNode = nextNode.next
        return result, visited


    def dfs_traversal(self, graph, source):
        results = ""
        results += str(source)
        convertedSource = self.graph[source]
        numOfVertices = self.keys
        # edge case
        if numOfVertices is 0:
            return result
        
        # create a list to hold the number of visited nodes and mark them as False when visited
        visited = []
        for _ in range(numOfVertices):
            visited.append(False)
        
        # start the DFS from source
        result, visited = self.dfs_traversal_helper(graph, convertedSource, source, visited)
        results +=result
        # visit the remaining nodes in the list
        for numericSouce in range(self.keys):
            # Get the current adjacent node in the list
            convertedSource = self.graph[numericSouce]
            if visited[numericSouce] is False:
                result_new, visited = self.dfs_traversal_helper(graph, convertedSource, numericSouce, visited)
                results += result_new
        return results 

        # A function used by DFS
    # def DFSUtil(self, v, visited):
 
    #     # Mark the current node as visited
    #     # and print it
    #     visited.add(v)
    #     print(v, end=' ')
 
    #     # Recur for all the vertices
    #     # adjacent to this vertex
    #     for neighbour in range(self.keys):
    #         if neighbour not in visited:
    #             self.DFSUtil(neighbour, visited)
 
    # # The function to do DFS traversal. It uses
    # # recursive DFSUtil()
    # def DFS(self, graph, v):
    #     # Create a set to store visited vertices
    #     visited = set()
 
    #     # Call the recursive helper function
    #     # to print DFS traversal
    #     self.DFSUtil(v, visited)

def main():
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    graph.print_graph()
    #res = graph.DFS(graph, 1)
    #res = graph.dfs_traversal(graph, 1)
    #print(res)

main()



'''

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited

'''