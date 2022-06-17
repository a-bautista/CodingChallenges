'''
    1 ----> 2
    |  \    |
    |   \   |
    v    \  v
    3       4

    Input: graph = [[1,2],[1,4],[1,3],[2,4]], target = 4
    Output: [[1, 2, 4], [1, 4]]
    Explanation: There are two paths: 1 -> 2 -> 4 and 1 -> 4

    0: [1,2]
    1: [3]
    2: [3]
    3: []

'''
from collections import defaultdict
def solve(graph, target):
    adjacencyList = defaultdict(list)
    #target = len(graph)
    res = []
    visited = set()

    for A, B in graph:
        adjacencyList[A].append(B)
        adjacencyList[B].append(A)
    
    #print(adjacencyList)
    def backtrack(currentNode,currentPath):
        
        visited.add(currentNode)
        if currentNode==target:
            res.append(list(currentPath))

        for adjacentNode in adjacencyList[currentNode]:
            if adjacentNode not in visited:
                currentPath.append(adjacentNode)
                backtrack(adjacentNode, currentPath)
                currentPath.pop()
                visited.remove(adjacentNode)


    backtrack(1, [1])
    return res


def main():
    # below is a cleaner way to represent this graph from above instead of using 
    graph = [[1,2],[1,4],[1,3],[2,4]]
    res = solve(graph, 4)
    print(res)

main()