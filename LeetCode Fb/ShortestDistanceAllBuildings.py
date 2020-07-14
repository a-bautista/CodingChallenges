from collections import deque

class Solution:
    def shortestDistance(self, grid):
        h = len(grid)
        w = len(grid[0])

        distance = [[0 for _ in range(w)] for _ in range(h)]
        reach = [[0 for _ in range(w)] for _ in range(h)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        buildingNum = 0


        for i in range(h):
            for j in range(w):
                # once you find a building then start iterating the entire grid to calculate
                # the reach and distance. The isVisited matrix will be reset for every building.
                if grid[i][j] == 1:
                    buildingNum += 1
                    q = deque()
                    # use the queue to visit every point in the grid
                    q.append((i, j, 0))

                    isVisited = [[False for _ in range(w)] for _ in range(h)]

                    while q:

                        x, y, d = q.popleft()
                        for dx, dy in directions:
                            x_cursor = x + dx
                            y_cursor = y + dy

                            if 0 <= x_cursor < h and 0 <= y_cursor < w and grid[x_cursor][y_cursor] == 0 \
                                    and not isVisited[x_cursor][y_cursor]:
                                distance[x_cursor][y_cursor] += d + 1
                                reach[x_cursor][y_cursor] += 1

                                isVisited[x_cursor][y_cursor] = True
                                q.append((x_cursor, y_cursor, d + 1))


        # from the distance grid, determine the shortest point
        shortest = float("inf")
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1

'''
    Time complexity: O(M*N)
    Space complexity: O(M*N)
'''

def main():
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    solution = Solution()
    res = solution.shortestDistance(grid)
    print(res)


main()