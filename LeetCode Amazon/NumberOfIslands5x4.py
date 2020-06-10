from typing import List

def main():
    #solution1 = Solution1.numIslands(Solution1,[['1', '1', '1', '1', '0'],
    #                                            ['1', '1', '0', '1', '0'],
    #                                            ['1', '1', '0', '0', '0'],
    #                                            ['0', '0', '0', '0', '0']
    #                                         ])

    solution2 = Solution2.numIslands(Solution2,[ [['1', '0', '0', '0', '0', '0', '0'],
                                                  ['0', '1', '0', '0', '0', '0', '0'],
                                                  ['0', '0', '1', '0', '0', '0', '0'],
                                                  ['0', '0', '0', '1', '0', '0', '0'],
                                                  ['0', '0', '0', '0', '1', '0', '0'],
                                                  ['0', '0', '0', '0', '0', '1', '0'],
                                                  ['0', '0', '0', '0', '0', '0', '1'],
     ]])

    solution3 = Solution3.numIslands(Solution3,[[['1', '0', '0', '0', '0', '0', '0'],
                                                  ['0', '1', '0', '0', '0', '0', '0'],
                                                  ['0', '0', '1', '0', '0', '0', '0'],
                                                  ['0', '0', '0', '1', '0', '0', '0'],
                                                  ['0', '0', '0', '0', '1', '0', '0'],
                                                  ['0', '0', '0', '0', '0', '1', '0'],
                                                  ['0', '0', '0', '0', '0', '0', '1'],
     ]])


    solution1 = Solution1.numIslands(Solution1, [['1', '1', '0', '0'],
['0', '0', '0', '0'],
['0', '0', '1', '1'],
['0', '0', '0', '0']]
     )



    print(solution1)
    #print(solution2)
    # print(solution3)


'''
['1', '1', '0', '0'],
['0', '0', '0', '0'],
['0', '0', '1', '1'],
['0', '0', '0', '0'],
                                                  ['0', '0', '0', '1', '0', '0', '0'],
                                                  ['0', '0', '0', '0', '1', '0', '0'],
                                                  ['0', '0', '0', '0', '0', '1', '0'],
                                                  ['0', '0', '0', '0', '0', '0', '1'],

'''




# set 1
# ['1', '1', '0', '1', '1'],
# ['1', '0', '0', '0', '0'],
# ['0', '0', '0', '0', '1'],
# ['1', '1', '0', '1', '1']]
# result = 4


# set 2
# ['1', '1', '0', '0', '0']
# ['1', '1', '0', '0', '0']
# ['0', '0', '1', '0', '0']
# ['0', '0', '0', '1', '1']
# result = 3


# set 3
# ['1', '1', '1', '1', '0']
# ['1', '1', '0', '1', '0']
# ['1', '1', '0', '0', '0']
# ['0', '0', '0', '0', '0']
# result = 1



# set 4 This doesn't work because the grid is 5x5
# ['1', '1', '0', '0', '0'],
# ['0', '1', '0', '0', '1'],
# ['1', '0', '0', '1', '1'],
# ['0', '0', '0', '0', '0'],
# ['1', '0', '1', '0', '1']
# result = 5


class Solution1:
    def numIslands(self, grid: List[List[int]]) -> int:
        print(grid)
        if grid == []:
            return 0

        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for i in range(n)]

        def bfs(i, j):
            visited[i][j] = 1
            queue = [(i, j)]
            while queue:
                # print(queue)
                point = queue.pop(0)
                i = point[0]
                j = point[1]
                if i > 0 and visited[i - 1][j] == 0 and grid[i - 1][j] == "1":
                    queue.append((i - 1, j))
                    visited[i - 1][j] = 1

                if j > 0 and visited[i][j - 1] == 0 and grid[i][j - 1] == "1":
                    queue.append((i, j - 1))
                    visited[i][j - 1] = 1

                if i < n - 1 and visited[i + 1][j] == 0 and grid[i + 1][j] == "1":
                    queue.append((i + 1, j))
                    visited[i + 1][j] = 1

                if j < m - 1 and visited[i][j + 1] == 0 and grid[i][j + 1] == "1":
                    queue.append((i, j + 1))
                    visited[i][j + 1] = 1

            return

        count = 0
        # bfs(0,0)
        # print(visited)

        for i in range(n):
            for j in range(m):
                # print(visited)
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    bfs(i, j)

        return count


def doBfs(grid, i, j):
    deq = []
    deq.append([i, j])
    while deq:
        x, y = deq.pop()
        grid[x][y] = "v"  # visited
        if x + 1 < len(grid) and grid[x + 1][y] == "1":
            deq.append([x + 1, y])
        if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
            deq.append([x, y + 1])
        if y - 1 >= 0 and grid[x][y - 1] == "1":
            deq.append([x, y - 1])
        if x - 1 >= 0 and grid[x - 1][y] == "1":
            deq.append([x - 1, y])


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    doBfs(grid, i, j)
                    count += 1
        return count



class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for i in range(n)]

        def bfs(i, j):
            visited[i][j] = 1
            queue = [(i, j)]
            while queue:
                # print(queue)
                point = queue.pop(0)
                i = point[0]
                j = point[1]
                if i > 0 and visited[i - 1][j] == 0 and grid[i - 1][j] == "1":
                    queue.append((i - 1, j))
                    visited[i - 1][j] = 1

                if j > 0 and visited[i][j - 1] == 0 and grid[i][j - 1] == "1":
                    queue.append((i, j - 1))
                    visited[i][j - 1] = 1

                if i < n - 1 and visited[i + 1][j] == 0 and grid[i + 1][j] == "1":
                    queue.append((i + 1, j))
                    visited[i + 1][j] = 1

                if j < m - 1 and visited[i][j + 1] == 0 and grid[i][j + 1] == "1":
                    queue.append((i, j + 1))
                    visited[i][j + 1] = 1

            return

        count = 0
        # bfs(0,0)
        # print(visited)

        for i in range(n):
            for j in range(m):
                # print(visited)
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    bfs(i, j)

        return count


if '__main__' == __name__:
    main()


''' Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water 
    and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are 
    all surrounded by water.'''