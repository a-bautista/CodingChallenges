from collections import deque


def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    # copy the lists of lists
    matrix = [row[:] for row in m]
    # print(matrix)

    # get the total rows # and total columns #
    nrow, ncol = len(matrix), len(matrix[0])

    # tuple of tuples in a double ended queue contained in a list
    # you can add elements to the right (q.append()) or to the left (q.appendleft())
    q = deque([((0, 0), 0)])  # ((x, y), step)
    # print(q)

    matrix[0][0] = "D"
    while q:
        # set the values to (0,0), 0 and make the double ended queue empty, so when you find an incorrect path then the steps that were used will be deleted
        (x, y), step = q.popleft()

        print((x, y), step)

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            # print(dx)

            if 0 <= x + dx < nrow and 0 <= y + dy < ncol:
                if matrix[x + dx][y + dy] == "X":
                    print('Treasure found!')
                    return step + 1
                elif matrix[x + dx][y + dy] == "O":
                    # mark visited
                    matrix[x + dx][y + dy] = "D"
                    q.append(((x + dx, y + dy), step + 1))
                    print(q)

    return -1


if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]

    res = solution(treasure_map)
    print("Result: ", res)