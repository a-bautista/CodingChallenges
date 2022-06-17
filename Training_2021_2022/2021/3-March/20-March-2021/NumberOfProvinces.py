'''
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are 
directly connected, and isConnected[i][j] = 0 otherwise.

            0 1 2 3
        0: [1,0,0,1],
        1: [0,1,1,0],
        2: [0,1,1,1],
        3: [1,0,1,1]

        visited = [0, 0, 0, 0]
        Get the first element of adjacent list, mark it as visited and if this element is 1 and its position in the 
        visited list is 0 then add it to the queue, else continue traversing the same list. Once you find an element 1 
        that hasn't been visited then go to the position of that element in the keys of the adjacent lists, for instance,
        there's a 1 in list 0 position 3, then go to the list 3 and start traversing all the elements 1. 

'''

# we define this array to mark the visited nodes because we will traverse this node as adjacent lists
from collections import deque
def solve(grid):
    visited = [0] * len(grid)
    count = 0
    queue = deque()
    for i in range(len(grid)):
        if visited[i] == 0:
            queue.append(i)
            while queue:
                currentAdjacentNode = queue.popleft()
                visited[currentAdjacentNode] = 1
                for j in range(len(grid)):
                    if grid[currentAdjacentNode][j] == 1 and visited[j] == 0:
                        queue.append(j)
            count += 1
    return count

def main():
    isConnected =  [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    isConnected2 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    res = solve(isConnected2)
    print(res)

main()