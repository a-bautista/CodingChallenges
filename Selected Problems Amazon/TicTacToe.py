class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.rowv = [0] * n
        self.colv = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row, col, player):
        player_val = 1
        if player == 2:
            player_val = -1

        self.rowv[row] += player_val
        self.colv[col] += player_val

        if row == col:
            self.diag1 += player_val
            if abs(self.diag1) == self.n:
                return player
        if (self.n - 1 - row) == col:
            self.diag2 += player_val
            if abs(self.diag2) == self.n:
                return player

        if abs(self.rowv[row]) == self.n or abs(self.colv[col]) == self.n:
            return player
        else:
            return 0

def main():
    tictactoe = TicTacToe(3)
    tictactoe.move(0, 0, 1)
    tictactoe.move(0, 1, 1)
    tictactoe.move(0, 2, 1)
    tictactoe.move(2, 0, 2)
    tictactoe.move(2, 1, 2)
    tictactoe.move(2, 2, 2)
    #print(param_1)


class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row]+=1 if player==1 else -1
        self.col[col]+=1 if player==1 else -1
        if row+col==self.n-1:
            self.diag1+=1 if player==1 else -1
        if row-col==0:
            self.diag2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return 1 if player==1 else 2
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)