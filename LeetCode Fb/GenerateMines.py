'''
    You are given a m*n grid. You are asked to generate k mines on this grid randomly.
    Each cell should have equal probability of k / m*n of being chosen

'''

import random

# m,n : Size of grid
# k : Number of mines
def plant(m,n,mines):
    board = m*n
    delimiter_bomb = board
    results = []
    # [0,0,0,0,0,0,0] will hold the bombs as [1,0,0,0,1,0,1,0,0] in case m=n=k=3
    vector = [0] * board

    # start planting the mines in the vector
    for i in range(mines):
        bomb = random.randint(0,delimiter_bomb-1)
        vector_position = 0
        planted_bomb = 0
        for i in range(board):
            if vector[i]==0:
                # Empty cell to plant a bomb
                if vector_position==bomb:
                    # Found the p-th empty cell
                    planted_bomb = i
                    break
                vector_position += 1

        # contains the ith numbers where bombs are located in the vector
        results.append(planted_bomb)
        # plant the bomb in the vector
        vector[planted_bomb] = 1 # Block the cell
        # decrease the bomb delimiter because we have 1 space less once a bomb has been planted
        delimiter_bomb -= 1

    # i%m indicates the location of x and i//m indicates the location of y
    results = [(i%m,i//m) for i in results]
    return results


def main():
    k_mines = 3
    width = 3
    height = 3
    res = plant(width, height, k_mines)
    print(res)

main()

'''
    Time complexity: O(Mkn)
'''