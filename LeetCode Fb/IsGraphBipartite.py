'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

[
 [1,3], index 0 
 [0,2], index 1
 [1,3], index 2
 [0,2] index 3
 ]

'''

# solution 1 BFS
from collections import deque

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # this dictionary is going to store each node and the color that was used for coloring it. The idea is to get the 
        # following data structure: {0:1, 1:-1,2:1,3:-1}. This dictionary indicates that for each node, a different color
        # was used. 

        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, seen) == False:
                    return False
        return True

    # BFS (queue)
    def check(self, graph, start, seen):
        q = deque()
        # start coloring the graph
        q.append([start, 1])
        
        while q:
            pop, color = q.popleft()
            # In case you have already colored the nodes, then verify if the color is the same and if so, then skip and go onto
            # the next node in the queue
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            # define the index and the color that you will be using
            seen[pop] = color
            # get the next set of vertices that are connected to the current node
            vertices = graph[pop]
            # add the next nodes from the graph
            for v in vertices:
                # use -1 to change the color and append to the queue
                q.append((v, -color))
        return True
       
       
# solution 2 : DFS
       
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, 1, seen) == False:
                    return False
        return True

    def check(self, graph, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = graph[node]
        for v in vertices:
            if self.check(graph, v, -color, seen) == False:
                return False
        return True
        
        
def main():
    l = [[1,3],[0,2],[1,3],[0,2]]
    solution = Solution()
    res = solution.isBipartite(l)
    print(res)


main()

'''
    Time complexity: O(V+E)
    Space complexity: O(V+E)
'''