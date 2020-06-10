import sys
from collections import deque

def main():
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    shortestDistance(grid)

def shortestDistance(grid):
    if not grid: return 0

    rows = len(grid)
    cols = len(grid[0])

    distance = [[0 for _ in range(cols)] for _ in range(rows)]
    reach = [[0 for _ in range(cols)] for _ in range(rows)]

    buildings = 0

    for i in range(rows):
        for j in range(cols):
            # if there is a building update reach, distance for all zeros using BFS
            if grid[i][j] == 1:
                buildings += 1
                queue = deque([(i, j, 0)])

                visited = [[False for _ in range(cols)] for _ in range(rows)]

                while queue:
                    x, y, d = queue.popleft()
                    for x1, y1 in (0, 1), (0, -1), (1, 0), (-1, 0):
                        r = x + x1
                        c = y + y1

                        if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] == 0:
                            distance[r][c] += d + 1
                            reach[r][c] += 1
                            visited[r][c] = True
                            queue.append((r, c, d + 1))
    short = sys.maxsize
    # from distance get shortest distance if you can reach all nodes
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and reach[i][j] == buildings:
                short = min(short, distance[i][j])
    return short if short != sys.maxsize else -1


main()