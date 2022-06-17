'''
    1 ----- 2
    |  \    |
    |   \   |
    v    \  |
    3     \ 4

    Input: graph = [[1,2],[1,4],[1,3],[2,4]], target = 4
    Output: [[1, 2, 4], [1, 4]]
    Explanation: There are two paths: 1 -> 2 -> 4 and 1 -> 4

    1. Convert the list of lists into a graph, so you can have the following structure:

        1: [2, 4, 3]
        2: [1, 4]
        3: [1]
        4: [1, 2]

    2. 
        _o.O.o_

'''

from collections import defaultdict
def solve(graph, target):
    # ingredients
    dd = defaultdict(list)
    res = []
    visited = set()

    # convert the input into a graph with the mentioned structure of point 1.
    for A, B in graph:
        dd[A].append(B)
        dd[B].append(A)


    # backtrack
    def dfs(currentNode, target):
        visited.add(adjacentNode)
        if currentNode == target:
            res.append(list(currentNode))
        else:
            #for adjacentNode in dd[currentNode]:
            pass                

    
    dfs(1,[1])
    return 0    

    


def main():
    graph = [[1,2],[1,4],[1,3],[2,4]]
    target = 4
    res = solve(graph, target)
    

main()

