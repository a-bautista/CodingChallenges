from typing import List

def main():
    #solution1 = Solution1.numIslands(Solution1,[['1', '1', '1', '1', '0'],
    #                                            ['1', '1', '0', '1', '0'],
    #                                            ['1', '1', '0', '0', '0'],
    #                                            ['0', '0', '0', '0', '0']
    #                                         ])



    '''
    solution1 = numIslands([['1', '0', '0', '0', '0', '0', '0'],
                                                  ['0', '1', '0', '0', '0', '0', '0'],
                                                  ['0', '0', '1', '0', '0', '0', '0'],
                                                  ['0', '0', '0', '1', '0', '0', '0'],
                                                  ['0', '0', '0', '0', '1', '0', '0'],
                                                  ['0', '0', '0', '0', '0', '1', '0'],
                                                  ['0', '0', '0', '0', '0', '0', '1'],
     ],7,7)


    solution2 = numIslands([['1','1','0','0'],
                            ['0','0','0','0'],
                            ['0','0','1','1'],
                            ['0','0','0','0']],4,4)
    '''

    solution3 = numIslands(4,4,[[1, 1, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 1, 1],
                            [0, 0, 0, 0],

                            ])


    #print(solution1)
    #print(solution2)
    print(solution3)


def numIslands(rows, column, grid):
    print(grid)
    if grid == []:
        return -1

    #n = len(grid)
    #m = len(grid[0])
    #n = rows
    #m = column

    visited = [['O'] * column for _ in range(rows)]

    def bfs(i, j):
        visited[i][j] = 'X'
        queue = [(i, j)]
        while queue:
            # print(queue)
            point = queue.pop(0)
            i = point[0]
            j = point[1]
            if i > 0 and visited[i - 1][j] == 'O' and grid[i - 1][j] == 1:
                queue.append((i - 1, j))
                visited[i - 1][j] = 'X'

            if j > 0 and visited[i][j - 1] == 'O' and grid[i][j - 1] == 1:
                queue.append((i, j - 1))
                visited[i][j - 1] = 'X'

            if i < rows - 1 and visited[i + 1][j] == 'O' and grid[i + 1][j] == 1:
                queue.append((i + 1, j))
                visited[i + 1][j] = 'X'

            if j < column - 1 and visited[i][j + 1] == 'O' and grid[i][j + 1] == 1:
                queue.append((i, j + 1))
                visited[i][j + 1] = 'X'

        return

    count = 0
    # bfs(0,0)
    # print(visited)

    for i in range(rows):
        for j in range(column):
            # print(visited)
            if grid[i][j] == 1 and visited[i][j] == 'O':
                count += 1
                bfs(i, j)

    return count


'''def doBfs(grid, i, j):
    deq = []
    deq.append([i, j])
    while deq:
        x, y = deq.pop()
        grid[x][y] = "v"  # visited
        if x + 1 < len(grid) and grid[x + 1][y] == 1:
            deq.append([x + 1, y])
        if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
            deq.append([x, y + 1])
        if y - 1 >= 0 and grid[x][y - 1] == 1:
            deq.append([x, y - 1])
        if x - 1 >= 0 and grid[x - 1][y] == 1:
            deq.append([x - 1, y])
'''

if '__main__' == __name__:
    main()