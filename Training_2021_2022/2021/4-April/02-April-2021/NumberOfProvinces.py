'''
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city
    b, and city b is connected directly with city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city 
    are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    0: [1,0,0,1]
    1: [0,1,1,0]
    2: [0,1,1,0]
    3: [1,0,1,1]

    visited nodes
    [0,0,0,0]
'''
from collections import deque
def solve(grid):
    visited = [0]*len(grid)
    queue = deque()
    count = 0
    #sizeGrid = len(grid)
    for i in range(len(grid)):
        if visited[i]==0:
            queue.append(i)
            while queue:
                currentAdjacentNode = queue.popleft()
                visited[currentAdjacentNode]=1
                for j in range(len(grid)):
                    if grid[currentAdjacentNode][j]==1 and visited[j]==0:
                        queue.append(j)
            count+=1
    return count


def main():
    grid = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,1,1]]
    res = solve(grid)
    print(res)

main()