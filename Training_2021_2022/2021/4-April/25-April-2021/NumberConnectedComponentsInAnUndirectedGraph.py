'''
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] 
    indicates that there is an edge between ai and bi in the graph.

    Return the number of connected components in the graph.

    0---1    3
        |    |
        |    |
        2    4

    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    0--1   3
       |  /|
       | / |
       2/  4

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

'''
from collections import defaultdict, deque
def solve(edges, nodes):

    adjacencyList = defaultdict(list)
    queue = deque()
    count = 0
    visited = set()

    # convert the graph into an adjacency list
    for A, B in edges:
        adjacencyList[A].append(B)
        adjacencyList[B].append(A)
    
    # 
    for node in range(nodes):
        if node in visited:
            continue
        queue.append(node)
        # get all the adjacentNodes from the currentNode
        while queue:
            currentNode = queue.popleft()
            if currentNode in visited:
                continue
            visited.add(currentNode)
            for adjacentNode in adjacencyList[currentNode]:    
                queue.append(adjacentNode)
        count+=1
    return count


def main():
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    res = solve(edges, n)
    print(res)

main()