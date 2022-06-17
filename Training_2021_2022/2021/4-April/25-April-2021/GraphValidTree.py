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

        2. Then we can traverse the adjacency list with DFS.
        3. Mark each node as visited and once we have traversed them all then return if the length of the visited
            nodes is equal to n.
'''
from collections import defaultdict
def solve(edges, n):

    # make sure at the beginning that the number of edges is less than the number of nodes by a difference of 1
    if len(edges)!=n-1:
        return False

    
    # convert the input to an adjacency list
    adjacency_list = defaultdict(list)
    #adjacency_list = [[ for _ in range(n)]]

    # convert the input into an adjacency_list 
    for A, B in edges:
        # add the nodes bidirectionally
        adjacency_list[A].append(B)
        adjacency_list[B].append(A)

    
    # ingredients for BFS
    stack = [0]
    seen = set()
    seen.add(0)

    while stack:
        currentNode = stack.pop()
        for neighbor in adjacency_list[currentNode]:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            stack.append(neighbor)

    # if I was able to find all the nodes in the seen set then this graph can be converted into a tree    
    if len(seen)==n:
        return True

def main():
    edges = [[0,1],[0,2],[0,3],[1,4]]
    n = 5
    res = solve(edges, n)
    print(res)

main()


'''
    Let EEE be the number of edges, and NNN be the number of nodes.

    Time Complexity : O(N)O(N)O(N).

    When E≠N−1E ≠ N - 1E​=N−1, we simply return false. Therefore, the worst case is when E=N−1E = N - 1E=N−1. Because EEE is proportional to NNN, we'll say E=NE = NE=N to simplify the analysis.

    As said above, creating an adjacency list has a time complexity of O(N+E)O(N + E)O(N+E). Because EEE is now bounded by NNN, we can reduce this slightly to O(N+N)=O(N)O(N + N) = O(N)O(N+N)=O(N).

    The iterative breadth-first search and depth-first search are almost identical. Each node is put onto the queue/stack once, ensured by the seen set. Therefore, the inner "neighbour" loop runs once for each node. Across all nodes, the number of cycles this loop does is the same as the number of edges, which is simply NNN. Therefore, these two algorithms have a time complexity of O(N)O(N)O(N).

    The recursive depth-first search's "neighbour" loop runs only once for each node. Therefore, in total, the function is called once for each edge. So it is called $E = N times, and NNN of those times, it actually enters the "neighbour" loop. Collectively, the total number of iterations of the "neighbour" loop is E=NE = NE=N. So we get O(N)O(N)O(N), as these all simply add.

    Space Complexity : O(N)O(N)O(N).

    Previously, we determined that the adjacency list took O(E+N)O(E + N)O(E+N) space. We now know this is simply O(N)O(N)O(N).

    In the worst case, the search algorithms will require an additional O(N)O(N)O(N) space; this is if all nodes were on the stack/queue at the same time.

    So again we get a total of O(N)O(N)O(N).


'''
