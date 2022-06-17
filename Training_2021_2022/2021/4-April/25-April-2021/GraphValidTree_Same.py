'''
    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where 
    edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

    Return true if the edges of the given graph make up a valid tree, and false otherwise.

              0
            / | \
           1  2  3
           |
           4
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true


                0
                |
                1
              / | \
             3 -2  4

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false

    For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it can't possibly be fully 
    connected. Any more, and it has to contain cycles.

    Algorithm: Iterative DFS
        0. Verify if the number of edges is equal to n-1. If this is not the case then we conclude 
            that the graph cannot be a valid tree.

        1. First you need to convert the graph into an adjacency list because we want to transform this input 

            edges = [[0,1],[0,2],[0,3],[1,4]] 
                       0     1     2     3   

            to

            0: [1,2,3]
            1: [0,4]
            2: [0]
            3: [0]
            4: [1]

        2. Then we can traverse the adjacency list with DFS or BFS.
        3. Mark each node as visited and once we have traversed them all then return if the length of the visited
            nodes is equal to n.
'''

from collections import defaultdict
def solve(graph, n):
    
    # make sure at the beginning that the number of edges is less than the number of nodes by a difference of 1
    if len(graph)!=n-1:
        return False
    
    adjacencyList = defaultdict(list)
    
    
    # convert the graph into an adjacency list
    for A, B in graph:
        adjacencyList[A].append(B)
        adjacencyList[B].append(A)

    # ingredients for BFS
    stack = [0]
    visited = set()
    visited.add(0)


    for node in range(n):
        currentNode = stack.pop()

        for adjacentNode in adjacencyList[currentNode]:
            if adjacentNode in visited:
                continue
            visited.add(adjacentNode)
            stack.append(adjacentNode)

    return len(visited)==n


def main():
     n = 5
     edges = [[0,1],[0,2],[0,3],[1,4]]
     res = solve(edges, n)
     print(res)

main()