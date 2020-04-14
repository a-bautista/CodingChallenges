
def main():
    graph = [[1, 1, 1, 1, 0],
             [1, 1, 0, 1, 0],
             [1, 1, 0, 0, 1],
             [0, 0, 0, 0, 0]]

    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)

    expected = 1
    assert g.countIslands() == expected

    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)

    expected = 5
    assert g.countIslands() == expected


    graph = [[1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1]]

    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)

    expected = 4
    assert g.countIslands() == expected

    # this test fails because the result gives 1 but it should be 3
    graph = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1]]


    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)
    print(g.countIslands())
    expected = 3
    assert g.countIslands() == expected



def solve(m):

    visited = 1
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    # copy the lists of lists
    matrix = [row[:] for row in m]


#def visit(row, col, matrix):


class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

        # A function to check if a given cell

    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

        # A utility function to do DFS for a 2D

    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];

        # Mark this cell as visited

        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

                # The main function that returns

    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count

if __name__ == '__main__':
    main()

'''https://www.geeksforgeeks.org/find-number-of-islands/'''