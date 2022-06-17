'''
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
    find all possible paths from node 0 to node n - 1, and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
    (i.e., there is a directed edge from node i to node graph[i][j]).

    0 ----> 1
    |       |
    |       |
    v       v
    2 ----->3

    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

    0: [1,2]
    1: [3]
    2: [3]
    3: []

'''

def solve(graph):
    ans = []
    target = len(graph)-1
    def backtrack(currentNode, path):
        if currentNode==target:
            # you must create a new list for path, otherwise when you do a pop of the path then this will
            # affect the result of ans
            ans.append(list(path))
        
        # explore the adjacent nodes from the graph with DFS
        for nextNode in graph[currentNode]:
            path.append(nextNode)
            backtrack(nextNode, path)
            path.pop()

    # [0] is the path that we will follow from the 0 node 
    backtrack(0, [0])
    return ans

def main():
    graph = [[1,2],[3],[3],[]]
    res = solve(graph)
    print(res)

main()
